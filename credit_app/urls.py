from django.urls import path, include

from . import views

urlpatterns = [
    path('apps/', views.ApplicationListView.as_view(), name='apps_list'),
    path('apps/<int:pk>', views.ApplicationDetailView.as_view(), name='apps_detail'),
    path('apps/<int:pk>/update/', views.ApplicationUpdateView.as_view(), name='apps_update'),
    path('apps/<int:pk>/delete/', views.ApplicationDeleteView.as_view(), name='apps_delete'),

    path('clients/', views.ClientListView.as_view(), name='clients_list'),
    path('clients/create/', views.ClientCreateView.as_view(), name='clients_create'),
    path('clients/<int:pk>/', views.ClientDetailView.as_view(), name='clients_detail'),
    path('clients/<int:pk>/create_app', views.ApplicationCreateView.as_view(), name='apps_create'),
    path('clients/<int:pk>/update', views.ClientUpdateView.as_view(), name='clients_update'),
    path('clients/<int:pk>/delete', views.ClientDeleteView.as_view(), name='clients_delete'),

    path('', views.index, name='index'),
]
