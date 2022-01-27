from django_filters.rest_framework import FilterSet
from django_filters.filters import CharFilter, NumberFilter
from categories.models import Title


class TitleFilter(FilterSet):
    category = CharFilter(
        field_name='category__slug',
        lookup_expr='contains'
    )
    genre = CharFilter(
        field_name='genre__slug',
        lookup_expr='contains'
    )
    name = CharFilter(
        field_name='name',
        lookup_expr='contains'
    )
    year = NumberFilter(
        field_name='year',
        lookup_expr='exact'
    )

    class Meta:
        model = Title
        fields = ('name', 'year', 'genre', 'category')
