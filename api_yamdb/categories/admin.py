from django.contrib import admin
from .models import Genres, Title, Categories


@admin.register(Genres)
class GenreAmdin(admin.ModelAdmin):
    list_display = ('name',)
    empty_value_display = '-empty-'


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    empty_value_display = '-empty-'


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'year',
        'description',
        'category',
        'rating'
    )
    list_filter = ('category',)
    search_fields = ('name',)
    empty_value_display = '-empty-'
