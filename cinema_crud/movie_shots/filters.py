import django_filters as filters
from .models import MovieShots
from movie.models import Movie


class MovieShotsFilter(filters.FilterSet):
    movie = filters.ModelChoiceFilter(label='Название фильма', queryset=Movie.objects.all())
    title = filters.CharFilter(label='Заголовок')
    description = filters.CharFilter(label='Описание кадра')


    class Meta:
        model = MovieShots
        fields = ['movie', 'title', 'description']
