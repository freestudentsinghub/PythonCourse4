from django.db import models

from clients.models import Clients


class Message(models.Model):
    topic = models.CharField(max_length=150, verbose_name='Тема письма', help_text='Введите тему письма')
    body = models.TextField(verbose_name='Тело письма', help_text='Введите тело письма')

    def __str__(self):
        return f'{self.topic} {self.body}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['topic']


class Campaign(models.Model):
    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    ]

    first_sent_time = models.DateTimeField(null=True, blank=True, verbose_name='Дата первой отправки')
    end_time = models.DateTimeField(verbose_name='Дата окончания отправки')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created', verbose_name='Статус')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    recipients = models.ManyToManyField(Clients, verbose_name='Получатели')

    def __str__(self):
        return f'Рассылка {self.first_sent_time} - {self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['-end_time']



