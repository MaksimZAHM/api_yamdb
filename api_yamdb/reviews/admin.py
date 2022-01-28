from django.contrib import admin

from .models import Comment, Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'text', 'pub_date', 'score')
    search_fields = ('title', 'text', 'author')
    list_filter = ('pub_date', 'score',)
    empty_value_display = '-empty-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author', 'pub_date', 'review')
    search_fields = ('text', 'author',)
    list_filter = ('pub_date',)
    empty_value_display = '-empty-'
