import django_filters as filters
from .models import Seat
from screening.models import Screening

class SeatFilter(filters.FilterSet):
    seat_mpei = filters.NumberFilter(label='Номер места')
    available = filters.NumberFilter(label='Статус')
    screening = filters.ModelChoiceFilter(label='Номер сеанса', queryset=Screening.objects.all())
    class Meta:
        model = Seat
        fields = ['seat_mpei', 'available', 'screening']

