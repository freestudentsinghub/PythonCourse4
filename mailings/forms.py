from django.forms import ModelForm

from mailings.models import Message, Campaign


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        self.fields['topic'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите тему письма"
        })

        self.fields['body'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите тело письма"
        })


class CampaignForm(ModelForm):
    class Meta:
        model = Campaign
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super(CampaignForm, self).__init__(*args, **kwargs)

        self.fields['first_sent_time'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Дата первой отправки"
        })

        self.fields['end_time'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Дата окончания отправки"
        })

        self.fields['status'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Статус"
        })

        self.fields['message'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Сообщение"
        })

        self.fields['recipients'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Получатели"
        })



