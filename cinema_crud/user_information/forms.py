from django import forms
from .models import Booking

class BookingCreate(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('user', 'seat', 'screening')
        labels = {
            'user': ('Имя пользователя'),
            'screening': ('Номер сеанса'),
            'seat': ('Номер места')
        }
