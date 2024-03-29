# Generated by Django 3.2.3 on 2021-06-02 05:03

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(message='Имена могут содержать только Алфавитные символы', regex='^([А-Я]*[а-яё]*|[A-Z]*[a-z]*)$')], verbose_name='имя')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(message='Имена могут содержать только Алфавитные символы', regex='^([А-Я]*[а-яё]*|[A-Z]*[a-z]*)$')], verbose_name='фамилия')),
                ('phone', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Номер телефона должен быть введен в соответствии со следующим форматом: "0000000000".', regex='^[0-9]{10}$')], verbose_name='телефон')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(default=datetime.date.today, null=True, verbose_name='дата заявки')),
                ('product', models.CharField(choices=[('CS', 'Потреб'), ('CR', 'Авто'), ('PL', 'Залог'), ('MG', 'Ипотека')], max_length=8, verbose_name='продукт')),
                ('decision', models.CharField(blank=True, choices=[('AP', 'Одобренно'), ('DE', 'Отказано'), ('TD', 'Временный отказ')], max_length=11, null=True, verbose_name='решение')),
                ('decision_comment', models.TextField(blank=True, null=True, verbose_name='комментарий к решению')),
                ('client', models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='credit_app.client', verbose_name='клиент (номер телефона)')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
