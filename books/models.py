# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class User(models.Model):
    pass

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



class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    isbn = models.CharField(max_length=17)
    publisher = models.CharField(max_length=128)
    genre = models.IntegerField(choices=GENRES)
    available = models.BooleanField(default=True)

    def __str__(self):
        return '{} "{}"'.format(self.author, self.title)

