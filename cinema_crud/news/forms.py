from django import forms
from .models import News
from django.forms import Textarea, DateInput


class NewsCreate(forms.ModelForm):
    class Meta:
        model = News
        fields = ('image_news', 'date_news', 'title_news', 'description_news')
        labels = {
            'image_news': ('Снимок новости'),
            'date_news': ('Дата новости'),
            'title_news': ('Заголовок'),
            'description_news': ('Описание')
        }

        widgets = {
            'title_news': Textarea(attrs={'maxlength': 70, 'placeholder': 'Открытие ресторана'}),
            'description_news': Textarea(attrs={'maxlength': 1000, 'placeholder': 'Открыли новый ресторан при кинотеатре'}),
            'date_news': DateInput(attrs={'type': 'date'})
        }

