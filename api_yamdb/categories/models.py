import textwrap
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Genres(models.Model):
    name = models.CharField(
        'Name of genre',
        help_text='Name of genre',
        max_length=200,
        unique=True
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ('id', )

    def __str__(self):
        return f'{self.slug}'


class Categories(models.Model):
    name = models.CharField(
        'Name of categories',
        help_text='Name of categories',
        max_length=200,
        unique=True
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('id', )

    def __str__(self):
        return f'{self.slug}'


class Title(models.Model):
    name = models.CharField(
        'Name of titles',
        help_text='Name of titles',
        max_length=200
    )
    year = models.PositiveSmallIntegerField(
        'Release year of titles',
        help_text='Release year of titles',
        db_index=True
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Text of descriptions',
        help_text='Text of descriptions'
    )
    category = models.ForeignKey(
        Categories,
        verbose_name='Name of categories',
        help_text='Name of categories',
        related_name='categories',
        on_delete=models.SET_NULL,
        null=True
    )
    genre = models.ManyToManyField(
        Genres,
        verbose_name='Name of ganres',
        help_text='Name of ganres',
        through='TitlesGenres'
    )
    rating = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Score of ratings',
        help_text='Score of ratings',
        validators=(
            MinValueValidator(1),
            MaxValueValidator(10)
        )
    )

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
    genre = models.ForeignKey(
        Genres,
        related_name='titlesgenres',
        on_delete=models.CASCADE
    )
    title = models.ForeignKey(
        Title,
        related_name='titlesgenres',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.genre.slug}'
