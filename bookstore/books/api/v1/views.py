from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from books.models import Book, Author, Publisher, Genre
from books.api.v1.serializers import BookSerializer, AuthorSerializer, PublisherSerializer, GenreSerializer


class BasePagination(PageNumberPagination):
    """
    Базовый класс для разбивки на страницы для представлений API.
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20


class BookViewSet(viewsets.ModelViewSet):
    """
    Api эндпоинт, реализующий методы CRUD для книг.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # pagination_class = BasePagination


class AuthorViewSet(viewsets.ModelViewSet):
    """
    Api эндпоинт, реализующий методы CRUD для авторов.
    """
    queryset = Author.objects.all().order_by('full_name')
    serializer_class = AuthorSerializer
    pagination_class = BasePagination


class PublisherViewSet(viewsets.ModelViewSet):
    """
    Api эндпоинт, реализующий методы CRUD для издательств.
    """
    queryset = Publisher.objects.all().order_by('name')
    serializer_class = PublisherSerializer
    pagination_class = BasePagination


class GenreViewSet(viewsets.ModelViewSet):
    """
    Api эндпоинт, реализующий методы CRUD для жанров.
    """
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer
    pagination_class = BasePagination
