from django import forms
from .models import MovieShots
from django.forms import ModelForm, TextInput, Textarea


class MovieShotsCreate(forms.ModelForm):
    class Meta:
        model = MovieShots
        fields = ('image', 'movie', 'title', 'description')
        labels = {
            'image': ('Кадры из фильма'),
            'movie': ('Название фильма'),
            'title': ('Заголовок'),
            'description': ('Описание кадра')
        }


        widgets = {
            'title': TextInput(attrs={'maxlength': 70, 'placeholder': 'Кадр 1'}),
            'description': Textarea(attrs={'placeholder': 'Кадр на улице'})
        }


