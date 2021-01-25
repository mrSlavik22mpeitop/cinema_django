from django import forms
from .models import Branch
from django.forms import ModelForm, TextInput, NumberInput


class BranchCreate(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('name', 'seats')
        labels = {
            'name': ('Имя кинозала'),
            'seats': ('Количество мест')
        }

        widgets = {
            'name': TextInput(attrs={'maxlength': 70, 'placeholder': 'Юпитер'}),
            'seats': NumberInput(attrs={'maxlength': 40, 'placeholder': '250'})
        }
