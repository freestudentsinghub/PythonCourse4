from django.forms import ModelForm, forms

from clients.models import Clients


class ClientsForm(ModelForm):
    class Meta:
        model = Clients
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super(ClientsForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите почту"
        })

        self.fields['full_name'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите ФИО"
        })

        self.fields['comment'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите коментарий"
        })

