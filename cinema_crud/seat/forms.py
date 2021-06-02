from django import forms
from .models import Seat
from django.forms import ModelForm, NumberInput, BooleanField

class SeatCreate(forms.ModelForm):
    class Meta:
        model = Seat
        fields = ('seat_mpei', 'available', 'screening')
        labels = {
            'seat_mpei': ('Номер места'),
            'available': ('Статус'),
            'screening': ('Номер сеанса')
        }

        widgets = {
            'seat_mpei': NumberInput(attrs={'maxlength': 40, 'placeholder': '15'}),
        }