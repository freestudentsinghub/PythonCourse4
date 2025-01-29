from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from mailings.forms import MessageForm, CampaignForm
from mailings.models import Message, Campaign


class MessageListView(ListView):
    model = Message
    template_name = 'mailings/message_list.html'


class HomeView(TemplateView):
    template_name = "mailings/home.html"


class MessageDetailView(DetailView):
    model = Message


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailings:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:message_list')


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:message_list')


#Рассылки

class CampaignListView(ListView):
    model = Campaign
    template_name = 'mailings/campaign_list.html'


class CampaignDetailView(DetailView):
    model = Campaign


class CampaignDeleteView(DeleteView):
    model = Campaign
    success_url = reverse_lazy('mailings:campaign_list')


class CampaignUpdateView(UpdateView):
    model = Campaign
    form_class = CampaignForm
    success_url = reverse_lazy('mailings:campaign_list')


class CampaignCreateView(CreateView):
    model = Campaign
    form_class = CampaignForm
    success_url = reverse_lazy('mailings:campaign_list')

