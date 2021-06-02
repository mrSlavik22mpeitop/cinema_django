import django_filters as filters
from django.contrib.auth.models import User

class PersonFilter(filters.FilterSet):
    username = filters.CharFilter(label='Логин')
    first_name = filters.CharFilter(label='Имя')
    last_name = filters.CharFilter(label='Фамилия')
    email = filters.CharFilter(label='Почта')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
