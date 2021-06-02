from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from screening.models import Screening

class Seat(models.Model):
    seat_mpei = models.IntegerField()
    available = models.BooleanField(null=True)
    screening = models.ForeignKey('screening.Screening', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['id']


@receiver(post_save, sender=Screening)
def create_seats(sender, instance, created, *args, **kwargs):
    if created:
        number_of_seats = 36
        for i in range(number_of_seats):
            new_seat = Seat(seat_mpei=i+1, screening=instance, available=True)
            new_seat.save()
