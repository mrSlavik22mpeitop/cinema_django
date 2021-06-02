import django_filters as filters
from .models import Booking
from screening.models import Screening
from seat.models import Seat
from django.contrib.auth.models import User

class BookingFilter(filters.FilterSet):
    user = filters.ModelChoiceFilter(label='Имя пользователя', queryset=User.objects.all())
    screening = filters.ModelChoiceFilter(label='Номер сеанса', queryset=Screening.objects.all())
    seat = filters.ModelChoiceFilter(label='Номер места', queryset=Seat.objects.all())

    class Meta:
        model = Booking
        fields = ['user', 'screening', 'seat']