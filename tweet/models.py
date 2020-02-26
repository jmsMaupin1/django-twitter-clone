from django.db import models
from django.utils import timezone

from twitteruser.models import TwitterUser


# Create your models here.
class Tweet(models.Model):
    text = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(
        TwitterUser,
        default=None,
        on_delete=models.CASCADE
    )
