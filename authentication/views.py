from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout

from twitteruser.models import TwitterUser
from authentication.forms import LoginForm, RegisterForm


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))

    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = TwitterUser.objects.create_user(
                username=data['username'],
                password=data['password1']
            )
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))

    else:
        form = RegisterForm()

    return render(request, 'generic_form.html', {
        'form': form
    })
