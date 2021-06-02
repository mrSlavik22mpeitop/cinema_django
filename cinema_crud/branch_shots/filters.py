import django_filters as filters
from .models import BranchShots
from branch.models import Branch


class BranchShotsFilter(filters.FilterSet):
    branch = filters.ModelChoiceFilter(label='Название кинозала', queryset=Branch.objects.all())
    title = filters.CharFilter(label='Заголовок')
    description = filters.CharFilter(label='Описание кадра')


    class Meta:
        model = BranchShots
        fields = ['branch', 'title', 'description']
