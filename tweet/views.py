import re

from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from tweet.forms import TweetForm
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import Notification


# Create your views here.
class IndexModelView(LoginRequiredMixin, View):
    form_class = TweetForm
    template = 'index/index.html'

    def notify(self, tweet):
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

    def build_context(self, user):
        tweets = None
        users = None
        notifications = None

        try:
            following = list(user.following.all())
            users = TwitterUser.objects.all()
            following.append(user)
            notifications = Notification.objects.filter(recipient=user)

            tweets = Tweet.objects \
                .filter(created_by__in=following) \
                .order_by('-created_at')
        except Exception:
            pass

        return {
            'form': self.form_class(),
            'tweets': tweets,
            'users': users,
            'notifications': notifications
        }

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.created_by = TwitterUser.objects.get(id=request.user.id)
            tweet.save()
            self.notify(tweet)

        context = self.build_context(request.user)
        return render(request, self.template, context)

    def get(self, request, *args, **kwargs):
        context = self.build_context(request.user)
        return render(request, self.template, context)


class TweetDetailView(View):
    template = 'tweet-detail.html'
    tweet = None
    users = None

    def get(self, request, tweet_id):
        try:
            self.users = TwitterUser.objects.all()
            self.tweet = Tweet.objects.get(id=tweet_id)
        except Exception:
            return HttpResponseRedirect(reverse('homepage'))

        return render(request, self.template, {
            'tweet': self.tweet,
            'users': self.users
        })
