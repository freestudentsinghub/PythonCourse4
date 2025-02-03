from django.contrib import messages
from django.core.mail import send_mass_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from mailings.forms import MessageForm, CampaignForm, SendCampaignForm
from mailings.models import Message, Campaign
from mailings.services import clean_emails


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


def send_campaign_view(request, pk=None):
    if pk:
        campaign = get_object_or_404(Campaign, pk=pk)
        initial_data = {'message': campaign.message,
                        'recipients': ','.join(campaign.recipients.values_list('email', flat=True))}
    else:
        campaign = None
        initial_data = {}

    if request.method == 'POST':
        form = SendCampaignForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            recipients = form.cleaned_data['recipients']
            cleaned_recipients = clean_emails(recipients)

            # Логика отправки рассылки
            mail_tuples = [(f'Рассылка', message, 'test.jango@yandex.ru', [recipient]) for recipient in cleaned_recipients]
            success_count = send_mass_mail(mail_tuples)

            messages.success(request, f'Письма успешно отправлены! Отправлено {success_count} писем.')
            return redirect('mailings:campaign_list')  # Переход на страницу успеха после отправки
    else:
        form = CampaignForm(initial=initial_data)

    context = {
        'form': form,
        'campaign': campaign,
    }
    return render(request, 'mailings/send_campaign.html', context)

