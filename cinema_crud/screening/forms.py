from django import forms
from .models import Screening
from django.forms import ModelForm, NumberInput, DateInput


class ScreeningCreate(forms.ModelForm):
    class Meta:
        model = Screening
        fields = ('movie_mpei', 'branch_mpei', 'screening_time', 'date_film', 'price')
        labels = {
            'movie_mpei': ('Название фильма'),
            'branch_mpei': ('Имя кинозала'),
            'screening_time': ('Длительность сеанса(минут)'),
            'date_film': ('Дата сеанса'),
            'price': ('Стоимость сеанса')
        }

        widgets = {
            'screening_time': NumberInput(attrs={'type': 'time'}),
            'date_film': DateInput(attrs={'type': 'date'}),
            'price': NumberInput(attrs={'maxlength': 40, 'placeholder': '237'})
        }
