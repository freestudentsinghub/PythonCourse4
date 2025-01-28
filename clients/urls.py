from django.contrib import admin
from django.urls import path, include

from clients.views import ClientsListView, HomeView, ClientsDetailView, ClientsDeleteView, ClientsCreateView, \
    ClientsUpdateView

app_name = 'clients'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('clients/list', ClientsListView.as_view(), name='clients_list'),
    path('clients/detail/<int:pk>', ClientsDetailView.as_view(), name='clients_detail'),
    path('clients/delete/<int:pk>', ClientsDeleteView.as_view(), name='clients_delete'),
    path('clients/create', ClientsCreateView.as_view(), name='clients_create'),
    path('clients/update/<int:pk>', ClientsUpdateView.as_view(), name='clients_update'),
]