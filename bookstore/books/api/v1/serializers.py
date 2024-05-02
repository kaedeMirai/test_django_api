from rest_framework import serializers

from books.models import Book, Author, Publisher, Genre


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id',
                  'title',
                  'description',
                  'author',
                  'genre',
                  'publishing_company',
                  'publication_date'
                  ]


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'full_name', 'about']


class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = ['id', 'name']


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'name']
