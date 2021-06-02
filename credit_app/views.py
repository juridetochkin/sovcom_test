from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import ModelFormMixin

from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from django_tables2.export.views import ExportMixin
from login_required import login_not_required

from .filters import ApplicationFilter, ClientFilter
from .models import Application, Client
from .forms import ApplicationForm, ClientForm
from .tables import ApplicationListTable, ApplicationLDetailTable, ClientListTable, \
    ClientDetailTable


@login_not_required
def index(request):
    """ Index page view """
    return render(request, 'index.html')


class ApplicationListView(SingleTableMixin, ExportMixin, FilterView):
    """
    Performs Applications listing, filtering, sorting, and the ability to export data.
    'django-tables2', 'tablib', 'django-filters' are used.
    """

    model = Application
    table_class = ApplicationListTable
    filterset_class = ApplicationFilter
    template_name = "apps_list.html"
    export_formats = ('csv', 'xls', 'xlsx')
    export_trigger_param = '_export'
    export_name = 'sovcom_apps'


class ApplicationCreateView(CreateView):
    """
    Creates new application.
    * Overridden form_valid() and get_context_data() to get
    * Clients 'pk' for template rendering and saving the instance.
    """

    form_class = ApplicationForm
    template_name = 'apps_create_or_update.html'
    pk_kwarg = None
    success_url = reverse_lazy('apps_list')

    def form_valid(self, form):
        client = Client.objects.get(pk=self.kwargs.get('pk'))
        self.object = form.save(commit=False)
        self.object.client = client
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

    def get_context_data(self, **kwargs):
        self.pk_kwarg = int(self.kwargs.get('pk'))
        ctx = super(ApplicationCreateView, self).get_context_data(**kwargs)
        ctx['client_pk'] = self.pk_kwarg
        return ctx


class ApplicationDetailView(SingleTableMixin, ExportMixin, DetailView):
    """
    Retrieves Application details.
    Also provides concrete application data exporting.
    * Overridden 'get_table_data()' to get a concrete application instead of queryset.
    """

    model = Application
    table_class = ApplicationLDetailTable
    template_name = 'detail.html'
    context_object_name = 'app'

    export_formats = ('csv', 'xls', 'xlsx')
    export_trigger_param = '_export'
    export_name = 'sovcom_apps'

    def get_table_data(self):
        return self.model.objects.filter(pk=self.kwargs.get('pk'))


class ApplicationUpdateView(UpdateView):
    """ Updates given application's data. """

    form_class = ApplicationForm
    queryset = Application.objects.all()
    template_name = 'apps_create_or_update.html'
    context_object_name = 'app'
    success_url = reverse_lazy('apps_list')


class ApplicationDeleteView(SingleTableMixin, DeleteView):
    """
    Deletes given application.
    * Overridden 'get_table_data()' to get a concrete application instead of queryset.
    """

    model = Application
    table_class = ApplicationLDetailTable
    template_name = 'delete_confirm.html'
    context_object_name = 'app'
    success_url = reverse_lazy('apps_list')

    def get_table_data(self):
        return self.model.objects.filter(pk=self.kwargs.get('pk'))


class ClientListView(SingleTableMixin, ExportMixin, FilterView):
    """
    Performs Clients listing, filtering, sorting, and the ability to export data.
    'django-tables2', 'tablib', 'django-filters' are used.
    """

    model = Client
    table_class = ClientListTable
    filterset_class = ClientFilter
    template_name = "clients_list.html"
    export_formats = ('csv', 'xls', 'xlsx')
    export_trigger_param = '_export'
    export_name = 'sovcom_clients'


class ClientCreateView(CreateView):
    """ Creates new client. """

    form_class = ClientForm
    template_name = 'clients_create_or_update.html'
    success_url = reverse_lazy('clients_list')


class ClientDetailView(SingleTableMixin, ExportMixin, DetailView):
    """
    Retrieves Client details.
    Also provides concrete application data exporting.
    * Overridden 'get_table_data()' to get a concrete client instead of queryset.
    """

    model = Client
    table_class = ClientDetailTable
    template_name = 'detail.html'
    context_object_name = 'client'
    table_pagination = {
        "per_page": 10
    }

    export_formats = ('csv', 'xls', 'xlsx')
    export_trigger_param = '_export'
    export_name = 'sovcom_clients'

    def get_table_data(self):
        return self.model.objects.filter(pk=self.kwargs.get('pk'))


class ClientUpdateView(UpdateView):
    """ Updates given client's data. """

    form_class = ClientForm
    queryset = Client.objects.all()
    template_name = 'clients_create_or_update.html'
    context_object_name = 'client'
    success_url = reverse_lazy('clients_list')


class ClientDeleteView(SingleTableMixin, DeleteView):
    """
    Deletes given client.
    * Overridden 'get_table_data()' to get a concrete application instead of queryset.
    """

    model = Client
    table_class = ClientListTable
    template_name = 'delete_confirm.html'
    context_object_name = 'client'
    success_url = reverse_lazy('clients_list')

    def get_table_data(self):
        return self.model.objects.filter(pk=self.kwargs.get('pk'))
