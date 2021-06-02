import django_filters as filters
from .models import News


class NewsFilter(filters.FilterSet):
    date_news = filters.DateFilter(label='Дата')
    description_news = filters.CharFilter(label='Описание')
    title_news = filters.CharFilter(label='Заголовок')

    class Meta:
        model = News
        fields = ['date_news', 'description_news', 'title_news']
