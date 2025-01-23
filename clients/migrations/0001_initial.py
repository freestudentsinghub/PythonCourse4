# Generated by Django 5.1.5 on 2025-01-23 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Введите свою почту', max_length=254, unique=True, verbose_name='Почта')),
                ('full_name', models.CharField(help_text='Введите свое фио', max_length=150, verbose_name='Ф.И.О.')),
                ('comment', models.TextField(blank=True, help_text='Введите комментарий', verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['email', 'full_name'],
            },
        ),
    ]