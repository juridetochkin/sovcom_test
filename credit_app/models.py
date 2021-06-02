import datetime
from django.db import models
from django.db.models.signals import post_delete, post_save
from django.core.validators import RegexValidator
from django.urls import reverse_lazy
from change_log.mixins import ChangeloggableMixin  # noqa
from change_log.signals import journal_save_handler, journal_delete_handler  # noqa


class Client(ChangeloggableMixin, models.Model):
    """
    Credit client class.

    * 'Char Field' is chosen for storing client numbers
    * according to given 'mask' in the Technical Task.
    * Can also use external libraries to store ph. numbers according to International Standards.
    """

    phone_validator = RegexValidator(
        regex=r'^[0-9]{10}$',
        message=f'Номер телефона должен быть введен'
                f' в соответствии со следующим форматом: "0000000000".'
    )

    names_validator = RegexValidator(
        regex=r'^([А-Я]*[а-яё]*|[A-Z]*[a-z]*)$',
        message=f'Имена могут содержать только Алфавитные символы'
    )

    first_name = models.CharField(
        validators=(names_validator,),
        max_length=30,
        blank=True,
        null=True,
        verbose_name='имя'
    )
    last_name = models.CharField(
        validators=(names_validator,),
        max_length=30,
        blank=True,
        null=True,
        verbose_name='фамилия'
    )
    phone = models.CharField(
        validators=(phone_validator,),
        max_length=10,
        unique=True,
        verbose_name='телефон')

    def __str__(self):
        return f'{self.pk} | {self.first_name} {self.last_name} {self.phone}'

    def get_absolute_url(self):
        return reverse_lazy('clients_detail', kwargs={'pk': self.pk})


class Application(ChangeloggableMixin, models.Model):
    """
    Defines a model of credit application.
    """

    PRODUCTS = (
        ('CS', 'Потреб'),
        ('CR', 'Авто'),
        ('PL', 'Залог'),
        ('MG', 'Ипотека'),
    )

    DECISIONS = (
        ('AP', 'Одобренно'),
        ('DE', 'Отказано'),
        ('TD', 'Временный отказ'),
    )

    date_created = models.DateTimeField(default=datetime.datetime.now,
                                    null=True, verbose_name='дата заявки')
    product = models.CharField(max_length=8, choices=PRODUCTS, verbose_name='продукт')
    client = models.ForeignKey(
        Client,
        max_length=10,
        on_delete=models.CASCADE,
        verbose_name='клиент (номер телефона)',
        related_name='applications'
    )
    decision = models.CharField(
        max_length=11,
        choices=DECISIONS,
        blank=True,
        null=True,
        verbose_name='решение', )
    decision_comment = models.TextField(blank=True, null=True, verbose_name='комментарий к решению')

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse_lazy('apps_detail', kwargs={'pk': self.pk})


post_save.connect(journal_save_handler, sender=Client)
post_delete.connect(journal_delete_handler, sender=Client)

post_save.connect(journal_save_handler, sender=Application)
post_delete.connect(journal_delete_handler, sender=Application)

