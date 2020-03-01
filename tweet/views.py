import re

from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from tweet.forms import TweetForm
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import Notification


def notify(tweet):
    mention_pattern = r'([@#][\w_-]+)'
    tag = re.match(mention_pattern, tweet.text)
    if tag:
        try:
            tagged_user = TwitterUser.objects.get(username=tag.group()[1:])
            Notification.objects.create(
                recipient=tagged_user,
                tweet=tweet
            )
        except Exception:
            pass

# Create your views here.
@login_required()
def index(request):
    tweets = None
    users = None
    notifications = None

    if request.method == 'POST':
        form = TweetForm(request.POST)

        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.created_by = TwitterUser.objects.get(id=request.user.id)
            tweet.save()
            notify(tweet)

    try:
        following = list(request.user.following.all())
        users = TwitterUser.objects.all()
        following.append(request.user)
        notifications = Notification.objects.filter(recipient=request.user)

        tweets = Tweet.objects \
            .filter(created_by__in=following) \
            .order_by('-created_at')
    except Exception:
        pass

    return render(request, 'index/index.html', {
        'form': TweetForm(),
        'tweets': tweets,
        'users': users,
        'notifications': notifications
    })


def tweet_detail_view(request, tweet_id):
    tweet = None
    users = None

    try:
        users = TwitterUser.objects.all()
        tweet = Tweet.objects.get(id=tweet_id)
    except Exception:
        return HttpResponseRedirect(reverse('homepage'))

    return render(request, 'tweet-detail.html', {
        'tweet': tweet,
        'users': users
    })
