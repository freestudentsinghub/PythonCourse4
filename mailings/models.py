from django.db import models


class Message(models.Model):
    topic = models.CharField(max_length=150, verbose_name='Тема письма', help_text='Введите тему письма')
    body = models.TextField(verbose_name='Тело письма', help_text='Введите тело письма')

    def __str__(self):
        return f'{self.topic} {self.body}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['topic']
