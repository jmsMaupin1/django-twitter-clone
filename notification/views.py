from django.shortcuts import render, reverse, HttpResponseRedirect

from notification.models import Notification
from twitteruser.models import TwitterUser


# Create your views here.
def notification_view(request):
    try:
        notifications = list(Notification.objects.filter(recipient=request.user))
        Notification.objects.filter(recipient=request.user).delete()
        users = TwitterUser.objects.all()
    except Exception:
        return HttpResponseRedirect(reverse('homepage'))

    return render(request, 'notifications.html', {
        'notifications': notifications,
        'users': users
    })
