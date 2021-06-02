from django.contrib import admin
from .models import Application, Client


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'date_created', 'product', 'client', 'decision', 'decision_comment')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'phone')
