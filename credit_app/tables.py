from django_tables2 import tables, Column, RelatedLinkColumn

from .models import Application, Client


class ApplicationListTable(tables.Table):
    """ Describes Application list table (django-tables2 package) """

    id = Column(
        linkify=True,
        orderable=True,
    )
    date_created = Column(orderable=True, initial_sort_descending=True)
    product = Column(orderable=False)
    client = RelatedLinkColumn(orderable=False, verbose_name='Телефон', accessor='client.phone')
    decision = Column(orderable=False)
    decision_comment = Column(orderable=False)

    class Meta:
        model = Application
        template_name = "django_tables2/bootstrap.html"


class ApplicationLDetailTable(tables.Table):
    """ Describes Application detail table (django-tables2 package) """

    id = Column(orderable=False)
    date_created = Column(orderable=False)
    product = Column(orderable=False)
    client = RelatedLinkColumn(orderable=False, verbose_name='Телефон', accessor='client.phone')
    decision = Column(orderable=False)
    decision_comment = Column(orderable=False)

    class Meta:
        model = Application
        template_name = "django_tables2/bootstrap.html"


class ClientListTable(tables.Table):
    """ Describes Clients list table (django-tables2 package) """

    id = Column(
        linkify=True,
        orderable=True,
        initial_sort_descending=True
    )
    phone = Column(orderable=False)

    class Meta:
        model = Client
        template_name = "django_tables2/bootstrap.html"


class ClientDetailTable(tables.Table):
    """ Describes Client detail table (django-tables2 package) """

    id = Column(orderable=False)
    phone = Column(orderable=False)

    class Meta:
        model = Client
        template_name = "django_tables2/bootstrap.html"