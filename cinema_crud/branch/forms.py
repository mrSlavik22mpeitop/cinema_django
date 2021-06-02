from django import forms
from .models import Branch
from django.forms import TextInput, Textarea


class BranchCreate(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('name', 'description')
        labels = {
            'name': ('Имя кинозала'),
            'description': ('Описание кинозала'),
            'quantum': ('Количество рядов')
        }

        widgets = {
            'name': TextInput(attrs={'maxlength': 70, 'placeholder': 'Юпитер'}),
            'description': Textarea(attrs={'maxlength': 1000, 'placeholder': 'Описание фильма'}),
        }

