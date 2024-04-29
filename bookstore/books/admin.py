from django.contrib import admin
from .models import Book, Author, Publisher, Genre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    list_filter = ('title', )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name',]
    list_filter = ('full_name',)


@admin.register(Publisher)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_filter = ('name',)


@admin.register(Genre)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_filter = ('name',)