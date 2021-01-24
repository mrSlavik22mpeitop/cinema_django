from django import forms
from .models import Movie
from django.forms import ModelForm, TextInput, NumberInput

class MovieCreate(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'author', 'genre', 'price')
        labels = {
            'title': ('Название фильма'),
            'author': ('Автор фильма'),
            'genre': ('Жанр'),
            'price': ('Бюджет($)')
        }

        widgets = {
            'title': TextInput(attrs={'maxlength': 70, 'placeholder': 'Аватар'}),
            'author': TextInput(attrs={'maxlength': 70, 'placeholder': 'Джеймс Кэмерон'}),
            'genre': TextInput(attrs={'maxlength': 40, 'placeholder': 'Фэнтези'}),
            'price': NumberInput(attrs={'maxlength': 40, 'placeholder': '237'})
        }
