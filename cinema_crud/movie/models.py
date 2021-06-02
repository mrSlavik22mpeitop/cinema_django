from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=70)
    author = models.CharField(max_length=70)
    genre = models.CharField(max_length=100)
    price = models.CharField(max_length=70)
    picture = models.ImageField(upload_to='media/', null=True, blank=True)
    country = models.CharField(max_length=70, null=True)
    tagline = models.TextField(max_length=270, null=True)
    actor = models.TextField(max_length=250, null=True)
    rating = models.IntegerField(null=True)
    description = models.TextField(null=True)
    date_premier = models.DateField(max_length=70, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']

