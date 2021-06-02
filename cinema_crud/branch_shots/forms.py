from django import forms
from .models import BranchShots
from django.forms import ModelForm, TextInput, Textarea


class BranchShotsCreate(forms.ModelForm):
    class Meta:
        model = BranchShots
        fields = ('image', 'branch', 'title', 'description')
        labels = {
            'image': ('Кадры кинозала'),
            'branch': ('Название кинозала'),
            'title': ('Заголовок'),
            'description': ('Описание кадра')
        }


        widgets = {
            'title': TextInput(attrs={'maxlength': 70, 'placeholder': 'Кадр 1'}),
            'description': Textarea(attrs={'placeholder': 'Места в кинозале Корея'})
        }


