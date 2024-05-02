import json
import http.client

from channels.generic.websocket import WebsocketConsumer


class BookConsumer(WebsocketConsumer):
    """
    WebSocket клиент для обработки действий, связанных с книгой.
    """
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data: str) -> None:
        """
        Метод вызываемый при получении сообщений из WebSocket.

        Args:
            text_data (str): Полученные текстовые данные от клиента.
        """
        text_data_json = json.loads(text_data)
        action = text_data_json.get('action')
    
        if action == 'retrieve':
            self.retrieve_book(text_data_json)
        if action == 'create':
            self.create_book(text_data_json)

    def retrieve_book(self, data=None) -> None:
        """
        Метод получения книг с помощью API и отправки их клиенту WebSocket.
        """
        host = '127.0.0.1'
        port = 8000
        path = '/api/v1/books/'
        connection = http.client.HTTPConnection(host, port)
        connection.request('GET', path)
        response = connection.getresponse()
        if response.status == 200:
            data = response.read().decode('utf-8')
            book_list = json.loads(data)
            self.send(text_data=json.dumps({
                'action': 'retrieve',
                'books': book_list
            }))
        else:
            self.send(text_data=json.dumps({
                'action': 'error',
                'message': f'Failed to retrieve books. Status code: {response.status}'
            }))
        connection.close()

    def create_book(self, data: dict) -> None:
        """
        Метод для создания нового объекта модели Book с помощью API, 
        с использованием полученных данных от клиента WebSocket. 

        Args:
            data (dict): Данные, содержащие информацию о новой книги.
        """
        host = '127.0.0.1'
        port = 8000
        path = '/api/v1/books/'
        headers = {'Content-type': 'application/json'}
        book_data = {
            'title': data.get('title'),
            'author': data.get('author'),
            'genre': data.get('genre'),
            'publishing_company': data.get('publisher'),
        }
        connection = http.client.HTTPConnection(host, port)
        connection.request('POST', path, json.dumps(book_data), headers)
        response = connection.getresponse()
        update_books = self.get_update_books(data)
        if response.status == 201:
            self.send(text_data=json.dumps({
                'action': 'create',
                'message': 'Book created successfully.',
                'books': update_books
            }))
        else:
            self.send(text_data=json.dumps({
                'action': 'error',
                'message': f'Failed to create book. Status code: {response.status}'
            }))
        connection.close()

    def get_update_books(self, data: dict) -> list:
        """
        Метод для получения обновленного списка книг.

        Args:
            data (dict): данные о созданой книги.
        Return:
            list: Обновленнный список книг.
        """
        current_books = []
        current_books.insert(0, data)
        return current_books