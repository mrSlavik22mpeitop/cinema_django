from django.db import models


class MovieShots(models.Model):
    title = models.CharField(max_length=70, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='handa/', null=True, blank=True)
    movie = models.ForeignKey('movie.Movie', on_delete=models.CASCADE)

    def __str__(self):
        return self.id

# Create your models here.
