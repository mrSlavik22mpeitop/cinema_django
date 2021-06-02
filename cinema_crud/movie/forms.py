from django import forms
from .models import Movie
from django.forms import ModelForm, TextInput, NumberInput, RadioSelect, Textarea, DateInput


class MovieCreate(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'author', 'genre', 'price', 'picture', 'country', 'tagline', 'actor', 'rating',
                  'description',
                  'date_premier')
        labels = {
            'title': ('Название фильма'),
            'author': ('Автор фильма'),
            'genre': ('Жанр'),
            'price': ('Бюджет($)'),
            'picture': ('Афиша'),
            'country': ('Страна'),
            'tagline': ('Слоган'),
            'actor': ('Актеры'),
            'rating': ('Рейтинг'),
            'description': ('Описание'),
            'date_premier': ('Дата выхода')
        }


        widgets = {
            'title': TextInput(attrs={'maxlength': 70, 'placeholder': 'Аватар'}),
            'author': TextInput(attrs={'maxlength': 70, 'placeholder': 'Джеймс Кэмерон'}),
            'genre': TextInput(attrs={'maxlength': 40, 'placeholder': 'Фэнтези'}),
            'price': TextInput(attrs={'maxlength': 70, 'placeholder': '1000000'}),
            'country': TextInput(attrs={'maxlength': 70, 'placeholder': 'Япония'}),
            'tagline': Textarea(attrs={'placeholder': 'Они пытались узнать имя'}),
            'actor': Textarea(attrs={'placeholder': 'Джеки Чан'}),
            'rating': NumberInput(attrs={'maxlength': 40, 'placeholder': '237'}),
            'description': Textarea(attrs={'placeholder': 'Описание фильма'}),
            'date_premier': DateInput(attrs={'type': 'date'})
        }



