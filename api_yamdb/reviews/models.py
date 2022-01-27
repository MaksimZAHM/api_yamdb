from categories.models import Title
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Reviews for that Title',
        help_text='Reviews for that Title',
        related_name='reviews'
    )
    text = models.TextField(
        verbose_name='Text of reviews',
        help_text='Text of reviews'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Author of reviews',
        help_text='Author of reviews',
        related_name='reviews'
    )
    score = models.PositiveSmallIntegerField(
        validators=(
            MinValueValidator(1),
            MaxValueValidator(10)
        )
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Release date of reviews',
        help_text='Release date of reviews',
        db_index=True
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('author', 'title'),
                name='unique review'),
        )
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        verbose_name='Comments to this Review',
        help_text='Comments to this Review',
        related_name='comments'
    )
    text = models.TextField(
        verbose_name='Text of comments',
        help_text='Text of comments',
        max_length=300
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Author of comments',
        help_text='Author of comments',
        related_name='comments'
    )
    pub_date = models.DateTimeField(
        verbose_name='Publication date of comments',
        help_text='Publication date of comments',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
