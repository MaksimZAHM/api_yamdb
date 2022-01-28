from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

ADMIN = 'admin'
MODERATOR = 'moderator'
USER = 'user'
ROLES = (
        (USER, 'Пользователь'),
        (ADMIN, 'Админ'),
        (MODERATOR, 'Модератор')
)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """ Создает и возввращет пользователя с привилегиями суперадмина. """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractUser):
    bio = models.TextField(
        max_length=1000,
        blank=True)
    email = models.EmailField(
        max_length=254,
        unique=True
    )
    role = models.CharField(
        choices=ROLES,
        default='user',
        max_length=20
    )
    confirmation_code = models.CharField(
        max_length=128,
        null=True,
        blank=True)

    def __str__(self):
        return User.username

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == MODERATOR or self.is_staff
