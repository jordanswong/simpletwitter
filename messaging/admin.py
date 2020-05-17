from django.contrib import admin
from messaging.models import Tweet, Hashtag
# Register your models here.

admin.site.register(Tweet)
admin.site.register(Hashtag)
