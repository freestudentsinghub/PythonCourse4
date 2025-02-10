from django.db import models

from clients.models import Clients
from users.models import CustomUser


class Message(models.Model):
    topic = models.CharField(
        max_length=150, verbose_name="Тема письма", help_text="Введите тему письма"
    )
    body = models.TextField(verbose_name="Тело письма", help_text="Введите тело письма")

    def __str__(self):
        return f"{self.topic} {self.body}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["topic"]


class Campaign(models.Model):
    STATUS_CHOICES = [
        ("created", "Создана"),
        ("started", "Запущена"),
        ("completed", "Завершена"),
    ]

    first_sent_time = models.DateTimeField(
        null=True, blank=True, verbose_name="Дата первой отправки"
    )
    end_time = models.DateTimeField(verbose_name="Дата окончания отправки")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="created", verbose_name="Статус"
    )
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, verbose_name="Сообщение"
    )
    is_active = models.BooleanField(default=True, verbose_name="активна")
    recipients = models.ManyToManyField(Clients, verbose_name="Получатели")
    successful_attempts = models.IntegerField(default=0)
    unsuccessful_attempts = models.IntegerField(default=0)
    sent_messages = models.IntegerField(default=0)
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"Рассылка {self.first_sent_time} - {self.status}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ["-end_time"]
        permissions = [
            ("can_disable_mailing", "Can disable mailing"),
        ]


class CampaignAttempt(models.Model):
    STATUS_CHOICES = [
        ("status_ok", "Успешно"),
        ("status_nok", "Не успешно"),
    ]

    date_attempt = models.DateTimeField(verbose_name="Дата и время попытки")
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, verbose_name="Статус попытки"
    )
    server_response = models.TextField(verbose_name="Ответ почтового сервера")
    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE,
        verbose_name="Рассылка",
        related_name="campaign",
    )

    def __str__(self):
        return f"{self.date_attempt} <{self.status}>"

    class Meta:
        verbose_name = "Попытка"
        verbose_name_plural = "Попытки"
        ordering = ["date_attempt", "status"]
