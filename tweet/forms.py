from django import forms
from tweet.models import Tweet


class TweetForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'tweet-text'}),
        max_length=140,
        label=''
    )

    class Meta:
        model = Tweet
        fields = [
            'text'
        ]
