from django.shortcuts import render, reverse, HttpResponseRedirect

from twitteruser.models import TwitterUser
from tweet.models import Tweet


def user_detail_view(request, user_id):
    user = None
    tweets = None
    try:
        user = TwitterUser.objects.get(id=user_id)
        users = TwitterUser.objects.all()
        tweets = Tweet.objects.filter(created_by=user)
    except Exception:
        return HttpResponseRedirect(reverse('homepage'))

    return render(request, 'profile.html', {
        'user': user,
        'tweets': tweets,
        'users': users
    })
