from django import forms
from .models import Screening
from django.forms import ModelForm, NumberInput, DateInput

class ScreeningCreate(forms.ScreeningForm):
    class Meta:
        model = Screening
        fields = ('movie_id', 'branch_id', 'screening_time', 'date_film', 'price')
        labels = {
            'movie_id': ('Название фильма'),
            'branch_id': ('Имя кинозала'),
            'screening_time': ('Длительность сеанса(минут)'),
            'date_film': ('Дата сеанса'),
            'price': ('Стоимость сеанса')
        }

        widgets = {
            'screening_time': NumberInput(attrs={'maxlength': 70, 'placeholder': '120'}),
            'date_film': DateInput(attrs={'type': 'date'}),
            'price': NumberInput(attrs={'maxlength': 40, 'placeholder': '237'})
        }
