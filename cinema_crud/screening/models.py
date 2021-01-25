from django.db import models


class Screening(models.Model):
    movie_id = models.ForeignKey('movie.Movie', on_delete=models.CASCADE)
    branch_id = models.ForeignKey('branch.Branch', on_delete=models.CASCADE)
    screening_time = models.IntegerField()
    date_film = models.DateField(max_length=70)
    price = models.IntegerField()

# Create your models here.
