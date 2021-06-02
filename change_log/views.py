from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from django_tables2.export.views import ExportMixin

from .filters import ChangeLogFilter
from .models import ChangeLog
from .tables import ChangeLogListTable


class ChangeLogListView(SingleTableMixin, ExportMixin, FilterView):
    """
    Performs ChangeLog listing, filtering, sorting, and the ability to export data.
    'django-tables2', 'tablib', 'django-filters' are used.
    """

    model = ChangeLog
    table_class = ChangeLogListTable
    filterset_class = ChangeLogFilter
    template_name = "logs_list.html"
    export_formats = ('csv', 'json')
    export_trigger_param = '_export'
    export_name = 'sovcom_logs'