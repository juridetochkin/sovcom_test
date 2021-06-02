from django.forms import ModelForm
from django.forms.widgets import NumberInput
from .models import Application, Client


class ApplicationForm(ModelForm):
    """ Form for creating and deleting Application """

    class Meta:
        model = Application
        fields = ['date_created', 'product', 'decision', 'decision_comment']
        labels = {
            'date_created': 'Введите дату поступления заявки (ДД.ММ.ГГГГ ЧЧ:ММ:СС)',
            'product': 'Выберите кредитный продукт',
            'decision': 'Выберите актуальное решение по заявке',
            'decision_comment': 'Введите текст комментария к решению ',
        }


class ClientForm(ModelForm):
    """ Form for creating and deleting Client """

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'phone']
        labels = {
            'first_name': 'Введите имя клиента',
            'product': 'Выберите фамилию клиента',
            'phone': 'Введите номер телефона клиента (в соответствии с маской: 0000000000)'
        }
