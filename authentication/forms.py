from django import forms
from django.contrib.auth.forms import UserCreationForm

from twitteruser.models import TwitterUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model = TwitterUser
        fields = [
            'username'
        ]
