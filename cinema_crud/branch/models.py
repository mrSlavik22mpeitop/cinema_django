from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

# Create your models here.
