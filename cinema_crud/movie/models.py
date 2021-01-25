from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=70)
    author = models.CharField(max_length=70)
    genre = models.CharField(max_length=40)
    price = models.IntegerField()

    def __str__(self):
        return self.title
