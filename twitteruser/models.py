from django.db import models
from django.contrib.auth.models import AbstractUser


class TwitterUser(AbstractUser):
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='twitter_followers'
    )

    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='twitter_following'
    )
