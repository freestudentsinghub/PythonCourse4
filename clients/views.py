from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from clients.forms import ClientsForm
from clients.models import Clients
from mailings.models import Campaign


class ClientsListView(ListView):
    model = Clients
    template_name = 'clients/clients_list.html'


class HomeView(TemplateView):
    template_name = "clients/home.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "SkyMail"
        context_data["count_campaign"] = Campaign.objects.count()
        context_data["active_campaign_count"] = Campaign.objects.filter(status="started").count()
        unique_clients_count = Campaign.objects.values('recipients').distinct().count()
        context_data["unique_clients_count"] = unique_clients_count
        return context_data


class ClientsDetailView(DetailView):
    model = Clients


class ClientsDeleteView(DeleteView):
    model = Clients
    success_url = reverse_lazy('clients:clients_list')


class ClientsUpdateView(UpdateView):
    model = Clients
    form_class = ClientsForm
    success_url = reverse_lazy('clients:clients_list')


class ClientsCreateView(CreateView):
    model = Clients
    form_class = ClientsForm
    success_url = reverse_lazy('clients:clients_list')
