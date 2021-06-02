import django_filters as filters
from .models import Movie

class MovieFilter(filters.FilterSet):
    title = filters.CharFilter(label='Название')
    author = filters.CharFilter(label='Автор')
    genre = filters.CharFilter(label='Жанр')
    price = filters.NumberFilter(label='Бюджет')
    country = filters.CharFilter(label='Страна')

    class Meta:
        model = Movie
        fields = ['title', 'author', 'genre', 'price', 'country']




