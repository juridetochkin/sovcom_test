import django_filters

from .models import ChangeLog


class ChangeLogFilter(django_filters.FilterSet):
    """ Performs Log queryset filtering (django-filters package) """

    class Meta:
        model = ChangeLog
        fields = {
            'changed': ['gte', 'lte'],
            'model': ['exact'],
            'record_id': ['exact'],
            'user': ['exact'],
            'action_on_model': ['exact'],
        }
        labels = {
            'changed': ''
        }
