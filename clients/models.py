from django.db import models

# Create your models here.


class Clients(models.Model):
    email = models.EmailField(unique=True, verbose_name='Почта', help_text='Введите свою почту')
    full_name = models.CharField(max_length=150, verbose_name='Ф.И.О.', help_text='Введите свое фио')
    comment = models.TextField(verbose_name='Комментарий', help_text='Введите комментарий', blank=True)

    def __str__(self):
        return f'{self.email} {self.full_name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['email', 'full_name']


