import textwrap
from django.db import models


class Genres(models.Model):
    name = models.CharField('Name of genre', max_length=200, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ('id', )

    def __str__(self):
        return f'{self.slug}'


class Categories(models.Model):
    name = models.CharField('Name of categories', max_length=200, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('id', )

    def __str__(self):
        return f'{self.slug}'


class Title(models.Model):
    name = models.CharField('Name of titles', max_length=200)
    year = models.PositiveSmallIntegerField(db_index=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Categories,
        related_name='categories',
        on_delete=models.SET_NULL, null=True
    )
    genre = models.ManyToManyField(Genres, through='TitlesGenres')
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'
        ordering = ('id', )

    def __str__(self):
        short_descrip = textwrap.shorten(
            self.description,
            width=100,
            placeholder='...'
        )

        return f'{self.name} {self.year} {short_descrip}'


class TitlesGenres(models.Model):
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.genre.slug}'
