from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput

class PersonCreate(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {
            'username': ('Логин'),
            'first_name': ('Имя пользователя'),
            'last_name': ('Фамилия пользователя'),
            'email': ('Почта')
        }

        widgets = {
            'username': TextInput(attrs={'maxlength': 100, 'placeholder': 'mrSlavik22'}),
            'first_name': TextInput(attrs={'maxlength': 80, 'placeholder': 'Вячеслав'}),
            'last_name': TextInput(attrs={'maxlength': 80, 'placeholder': 'Волгин'}),
            'email': EmailInput(attrs={'maxlength': 254, 'placeholder': 'volgin_slavochka@mail.ru'})
        }