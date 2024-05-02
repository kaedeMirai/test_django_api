from django.contrib import admin

from .models import Book, Author, Publisher, Genre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Конфигурация модели Book для админки.
    """
    list_display = ['id',
                    'title',
                    'get_list_authors',
                    'publishing_company',
                    'get_list_genres',
                    'publication_date'
                    ]
    list_filter = ('title', 'publication_date')
    filter_horizontal = ('author', 'genre')

    def get_list_authors(self, obj):
        return ', '.join([author.full_name for author in obj.author.all()])

    def get_list_genres(self, obj):
        return ', '.join([genre.name for genre in obj.genre.all()])


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Конфигурация модели Author для админки.
    """
    list_display = ['id', 'full_name',]
    list_filter = ('full_name',)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    """
    Конфигурация модели Publisher для админки.
    """
    list_display = ['id', 'name',]
    list_filter = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    Конфигурация модели Publisher для админки.
    """
    list_display = ['id', 'name',]
    list_filter = ('name',)
