from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=70)
    seats = models.IntegerField()

    def __str__(self):
        return self.name

# Create your models here.
