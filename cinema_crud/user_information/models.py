from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    seat = models.ForeignKey('seat.Seat', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    screening = models.ForeignKey('screening.Screening', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.screening

    class Meta:
        ordering = ['id']
