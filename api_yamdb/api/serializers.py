import datetime as dt
from django.conf import settings
from django.db.models import Avg
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from reviews.models import Comment, Review
from categories.models import Categories, Genres, Title


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        validators=(UniqueValidator(queryset=User.objects.all()),)
    )
    email = serializers.EmailField(
        max_length=254,
        validators=(UniqueValidator(queryset=User.objects.all()),)
    )

    class Meta:
        model = User
        fields = ('email', 'username')

    def validate_username(self, value):
        if value.lower() == settings.USER_ME:
            raise serializers.ValidationError(
                'Для имени нельзя использовать {value}'
            )
        return value


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    confirmation_code = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = (
            'username',
            'confirmation_code'
        )


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Review
        exclude = ('title', )

    def validate(self, data):
        if self.context['request'].method == 'PATCH':
            return data

        author = self.context['request'].user
        title_id = self.context['view'].kwargs.get('title_id')

        if Review.objects.filter(author=author, title=title_id).exists():
            raise serializers.ValidationError(
                'You can only leave one review '
            )
        return data

    def validate_score(self, value):
        if not 1 <= value <= 10:
            raise serializers.ValidationError(
                'enter a score from 1 to 10 '
            )
        return value


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        exclude = ('review', )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        exclude = ('id', )


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genres
        exclude = ('id', )


class CreateTitleSerializer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all()
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genres.objects.all(),
        many=True
    )

    class Meta:
        model = Title
        fields = '__all__'

    def validate_year(self, value):
        if value <= dt.datetime.now().year:
            return value
        raise serializers.ValidationError(
            'Ошибка года выпуска. Год не может быть больше текущего!'
        )

    def validate_category(self, value):
        if not Categories.objects.filter(slug=value).exists():
            raise serializers.ValidationError(
                'Категории с таким slug не существует'
            )
        return value

    def validate_genre(self, value):
        for genre in value:
            if not Genres.objects.filter(slug=genre).exists():
                raise serializers.ValidationError(
                    'Жанра с таким slug не существует'
                )
        return value


class TitleSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    category = CategorySerializer()
    genre = GenreSerializer(many=True)

    class Meta:
        model = Title
        fields = '__all__'

    def get_rating(self, obj):
        rating = obj.reviews.aggregate(Avg('score')).get('score__avg')
        if not rating:
            return None
        return round(rating)
