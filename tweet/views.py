from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from tweet.forms import TweetForm
from tweet.models import Tweet
from twitteruser.models import TwitterUser

# Create your views here.
@login_required()
def index(request):
    tweets = None
    if request.method == 'POST':
        form = TweetForm(request.POST)

        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.created_by = TwitterUser.objects.get(id=request.user.id)
            tweet.save()

    try:
        tweets = Tweet.objects.all()
    except Exception:
        pass

    return render(request, 'index/index.html', {
        'form': TweetForm(),
        'tweets': tweets
    })


def tweet_detail_view(request, tweet_id):
    tweet = None

    try:
        tweet = Tweet.objects.get(id=tweet_id)
    except Exception:
        return HttpResponseRedirect(reverse('homepage'))

    return render(request, 'tweet-detail.html', {
        'tweet': tweet
    })
