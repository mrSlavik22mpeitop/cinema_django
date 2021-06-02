from django.db import models


class Screening(models.Model):
    movie_mpei = models.ForeignKey('movie.Movie', on_delete=models.CASCADE)
    branch_mpei = models.ForeignKey('branch.Branch', on_delete=models.CASCADE)
    screening_time = models.CharField(max_length=70)
    date_film = models.DateField(max_length=70)
    price = models.IntegerField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['id']



# Create your models here.
