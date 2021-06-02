from django_tables2 import tables, Column

from .models import ChangeLog


class ChangeLogListTable(tables.Table):
    """ Describes ChangeLog list table (django-tables2 package) """

    changed = Column(orderable=True,)
    model = Column(orderable=False)
    record_id = Column(orderable=False)
    user = Column(orderable=False)
    action_on_model = Column(orderable=False)
    data = Column(orderable=False)
    ipaddress = Column(exclude_from_export=True)

    class Meta:
        model = ChangeLog
        template_name = "django_tables2/bootstrap.html"
        exclude = ('ipaddress',)