from django.contrib import admin
from django.contrib.auth.models import User
from books.models import Book, Logs

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'publisher', 'genre', 'isbn', 'available')

@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):

    list_display = ('book', 'user', 'date_get', 'return_date')