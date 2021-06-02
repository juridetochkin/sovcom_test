import django_filters
from .models import Application, Client


class ApplicationFilter(django_filters.FilterSet):
    """ Performs Application queryset filtering (django-filters package) """

    class Meta:
        model = Application
        fields = {
            'id': ['exact'],
            'client': ['exact'],
            'date_created': ['gte', 'lte'],
            'product': ['exact'],
            'decision': ['exact'],
        }


class ClientFilter(django_filters.FilterSet):
    """ Performs Client queryset filtering (django-filters package) """

    class Meta:
        model = Client
        fields = {
            'id': ['exact'],
            'first_name': ['exact'],
            'last_name': ['exact'],
            'phone': ['exact'],
        }