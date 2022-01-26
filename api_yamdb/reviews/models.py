from categories.models import Title
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User


class Review(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE,
                              related_name='reviews')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='reviews')
    score = models.PositiveSmallIntegerField(
        validators=(
            MinValueValidator(1),
            MaxValueValidator(10)))
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации отзыва',
                                    db_index=True,)

    class Meta:
        constraints = (
            models.UniqueConstraint(fields=('author', 'title'),
                                    name='unique review'),
        )
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name='comments')
    text = models.TextField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comments')
    pub_date = models.DateTimeField('Дата публикации комментария',
                                    auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'
