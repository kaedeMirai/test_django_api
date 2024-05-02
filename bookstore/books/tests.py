from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from books.models import Book, Author, Publisher, Genre


class BookViewSetTestCase(TestCase):
    """
    Тесты для проверки API для модели Book. BookViewSet.
    """
    def setUp(self):
        self.client = APIClient()
        self.book = Book.objects.create(title='Test book', description='Test description')
        self.author = Author.objects.create(full_name='Test author')
        self.publisher = Publisher.objects.create(name='Test publisher')
        self.genre = Genre.objects.create(name='Test genre')
        self.book.author.add(self.author)
        self.book.genre.add(self.genre)
        self.book.publishing_company = self.publisher

    def test_get_all_books(self):
        """
        Тест на получения списка книг.
        """
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        """
        Тест на успешное создание книги.
        """
        data = {
            'title': 'New book',
            'description': 'New description',
            'author': [self.author.id],
            'genre': [self.genre.id],
            'publishing_company': self.publisher.id
        }
        response = self.client.post(reverse('book-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_with_required_fields(self):
        """
        Тест на создание книги с без обязательных полей.
        """
        response = self.client.post(reverse('book-list'), {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('title' in response.data)
        self.assertTrue('author' in response.data)
