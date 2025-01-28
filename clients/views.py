from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from clients.models import Clients


class ClientsListView(ListView):
    model = Clients
    template_name = 'clients/clients_list.html'


class HomeView(TemplateView):
    template_name = "clients/home.html"


class ClientsDetailView(DetailView):
    model = Clients


class ClientsDeleteView(DeleteView):
    model = Clients
    success_url = reverse_lazy('clients:clients_list')


class ClientsUpdateView(UpdateView):
    model = Clients
    fields = ('email', 'full_name', 'comment',)
    success_url = reverse_lazy('clients:clients_list')


class ClientsCreateView(CreateView):
    model = Clients
    fields = ('email', 'full_name', 'comment',)
    success_url = reverse_lazy('clients:clients_list')
