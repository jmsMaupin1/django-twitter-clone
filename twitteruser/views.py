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

        cur_user = TwitterUser.objects.get(id=request.user.id)
        is_following = cur_user.following.filter(id=user_id).exists()
    except Exception:
        return HttpResponseRedirect(reverse('homepage'))

    return render(request, 'profile.html', {
        'user': user,
        'tweets': tweets,
        'users': users,
        'is_following': is_following
    })


def follow_user_view(request, user_id):
    user_to_follow = None
    current_user = None
    try:
        user_to_follow = TwitterUser.objects.get(id=user_id)
        current_user = TwitterUser.objects.get(id=request.user.id)

        current_user.following.add(user_to_follow)
    except Exception:
        pass

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unfollow_user_view(request, user_id):
    user_to_unfollow = None
    current_user = None

    try:
        user_to_unfollow = TwitterUser.objects.get(id=user_id)
        current_user = TwitterUser.objects.get(id=request.user.id)

        current_user.following.remove(user_to_unfollow)
    except Exception:
        pass

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
