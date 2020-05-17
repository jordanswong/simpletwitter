from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Tweet(models.Model):

    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Hashtag(models.Model):

    name = models.TextField(default='')
    tagged_tweets = models.ManyToManyField(Tweet, related_name='tags', verbose_name='hashtags')
