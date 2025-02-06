from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mass_mail
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from mailings.forms import MessageForm, CampaignForm, CampaignModeratorForm
from mailings.models import Message, Campaign, CampaignAttempt



class MessageListView(ListView):
    model = Message
    template_name = 'mailings/message_list.html'



class HomeView(TemplateView):
    template_name = "clients/home.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "SkyMail"
        context_data["count_campaign"] = Campaign.objects.count()
        context_data["active_campaign_count"] = Campaign.objects.filter(status="Запущена").count()
        unique_clients_count = Campaign.objects.values('recipients').distinct().count()
        context_data["unique_clients_count"] = unique_clients_count
        return context_data


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

    def dispatch(self, request, *args, **kwargs):
        # Проверяем, имеет ли пользователь право на просмотр списка клиентов
        if not request.user.has_perm('mailings.view_campaign'):
            return HttpResponseForbidden("У вас нет прав для просмотра списка рассылок.")
        return super().dispatch(request, *args, **kwargs)


class CampaignDetailView(DetailView):
    model = Campaign


class CampaignDeleteView(DeleteView):
    model = Campaign
    success_url = reverse_lazy('mailings:campaign_list')


class CampaignUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Campaign
    form_class = CampaignForm
    success_url = reverse_lazy('mailings:campaign_list')

    permission_required = 'mailings.can_disable_mailing'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = not self.object.is_active
        self.object.save()
        return redirect(self.success_url)

    def handle_no_permission(self):
        return HttpResponseForbidden("У вас нет прав для отключения рассылки.")

    def get_form_class(self):
        user = self.request.user
        if user.has_perm("mailings.can_disable_mailing"):
            return CampaignModeratorForm
        raise PermissionDenied

    def test_func(self):
        user = self.request.user
        obj = self.get_object()
        return user.has_perm("mailings.can_disable_mailing")


class CampaignCreateView(CreateView):
    model = Campaign
    form_class = CampaignForm
    success_url = reverse_lazy('mailings:campaign_list')


