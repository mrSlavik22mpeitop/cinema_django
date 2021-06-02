import django_filters as filters
from .models import Screening
from movie.models import Movie
from branch.models import Branch

class ScreeningFilter(filters.FilterSet):
    movie_mpei = filters.ModelChoiceFilter(label='Название фильма', queryset=Movie.objects.all())
    branch_mpei = filters.ModelChoiceFilter(label='Название кинозала', queryset=Branch.objects.all())
    screening_time = filters.CharFilter(label='Время сеанса')
    date_film = filters.DateFilter(label='Дата сеанса')
    price = filters.NumberFilter(label='Стоимость')

    class Meta:
        model = Screening
        fields = ['movie_mpei', 'branch_mpei', 'screening_time', 'date_film', 'price']




