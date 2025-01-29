from django.forms import ModelForm, forms

from mailings.models import Message


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



