from uuid import uuid4

from django.db import models


class UUIDMixin(models.Model):
    """
    Миксин для добавления уникального идентификатора UUID в моделях.
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True


class Book(UUIDMixin):
    """
    Модель Django, которая содержит книги.
    """
    title = models.CharField(max_length=255, verbose_name='title')
    description = models.TextField(blank=True, verbose_name='description')

    author = models.ManyToManyField('Author', verbose_name='authors')
    genre = models.ManyToManyField('Genre', verbose_name='genres')
    publishing_company = models.ForeignKey('Publisher',
                                           on_delete=models.CASCADE,
                                           verbose_name='publisher',
                                           null=True,
                                           blank=True)

    publication_date = models.DateField(verbose_name='date of publication',
                                        null=True,
                                        blank=True)

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __str__(self) -> str:
        return self.title
    

class Author(UUIDMixin):
    """
    Модель django, которая содержит авторов произведений.
    """
    full_name = models.CharField(max_length=150, verbose_name='first_name')
    about = models.TextField(blank=True, verbose_name='about')

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'
    
    def __str__(self) -> str:
        return self.full_name


class Publisher(UUIDMixin):
    """
    Модель django, которая содержит книжные издательства.
    """
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'publisher'
        verbose_name_plural = 'publishers'
    
    def __str__(self) -> str:
        return self.name


class Genre(UUIDMixin):
    """
    Модель django, которая содержит жанры для книг.
    """
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def __str__(self) -> str:
        return self.name