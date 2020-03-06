from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.views import View

from twitteruser.models import TwitterUser
from authentication.forms import LoginForm, RegisterForm


# Create your views here.
class AuthenticationForm(View):
    template = 'generic_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template, {'form': form})


class LoginFormView(AuthenticationForm):
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))


class RegisterFormView(AuthenticationForm):
    form_class = RegisterForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = TwitterUser.objects.create_user(
                username=data['username'],
                password=data['password1']
            )
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
