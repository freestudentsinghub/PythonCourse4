from django import forms
from django.contrib.auth.forms import UserCreationForm


from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2')



