from django.contrib import admin
from django.contrib.auth.models import User
from books.models import Book

# Register your models here.

@admin.register(Book)
class CoachAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'publisher', 'genre', 'isbn', 'available')
