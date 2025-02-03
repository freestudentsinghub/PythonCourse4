from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, verbose_name="Введите юзернейм")
    email = models.EmailField(unique=True, verbose_name="Введите почту")
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Введите номер телефона")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    country = models.CharField(blank=True, max_length=50, verbose_name="Введите страну проживания")
    token = models.CharField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.email

