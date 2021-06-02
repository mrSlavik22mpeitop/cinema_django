import django_filters as filters
from .models import Branch

class BranchFilter(filters.FilterSet):
    name = filters.CharFilter(label='Название кинозала')

    class Meta:
        model = Branch
        fields = ['name']
