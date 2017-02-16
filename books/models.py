# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site


GENRES = (
    (1, "Romans"),
    (2, "Obyczajowa"),
    (3, "Sci-fi i fantasy"),
    (4, "Literatura faktu"),
    (5, "Popularnonaukowa"),
    (6, "Poradnik"),
    (7, "Kryminał"),
    (8, "Klasyka"),
    (9, "Historia"),
    (10, "Poezja"),
    (11, "Przygodowa"),
    (12, "Bajki"),
    (13, "Komiks"),
    (14, "Dramat"),
    (15, "Literatura współczesna")
)

class Logs(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_get = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    return_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return '{} "{}"'.format(self.book, self.user)

class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    isbn = models.CharField(max_length=17)
    publisher = models.CharField(max_length=128)
    genre = models.IntegerField(choices=GENRES)
    available = models.BooleanField(default=True)
    lent_by = models.ManyToManyField(User, through='Logs')

    def __str__(self):
        return '{} "{}"'.format(self.author, self.title)

