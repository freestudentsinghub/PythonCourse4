from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from mailings.models import Campaign, CampaignAttempt


def run_mailing(request, pk):
    """Функция запуска рассылки по требованию"""
    campaign = get_object_or_404(Campaign, id=pk)
    for recipient in campaign.recipients.all():
        try:
            campaign.status = 'started'
            send_mail(
                subject=campaign.message.topic,
                message=campaign.message.body,
                from_email=EMAIL_HOST_USER,
                recipient_list=[recipient.email],
                fail_silently=False,
            )
            CampaignAttempt.objects.create(
                date_attempt=timezone.now(),
                status='status_ok',
                server_response="Email отправлен",
                campaign=campaign,
            )
        except Exception as e:
            print(f"Ошибка при отправке письма для {recipient.email}: {str(e)}")
            CampaignAttempt.objects.create(
                date_attempt=timezone.now(),
                status='status_nok',
                server_response=str(e),
                campaign=campaign,
            )
    if campaign.end_sending and campaign.end_sending <= timezone.now():
        # Если время рассылки закончилось, обновляем статус на "завершено"
        campaign.status = 'completed'
    campaign.save()
    return redirect("mailings:campaign_list")

@login_required
def block_mailing(request, pk):
    campaign = Campaign.objects.get(pk=pk)
    campaign.is_active = {campaign.is_active: False, not campaign.is_active: True}[True]
    campaign.save()
    return redirect(reverse("mailing:campaign_list"))