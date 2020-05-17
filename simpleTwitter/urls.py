"""simpleTwitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from about.views import splash
from accounts.views import login_view,logout_view,profile_view
from accounts.views import signup_view
from messaging.views import create_tweet,home_view,hashtags_view,delete_tweet,hashtags_filter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', splash, name='splash'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('myprofile/', profile_view, name='myprofile'),
    path('myprofile/tweet/', create_tweet, name='c_tweet'),
    path('myprofile/delete/', delete_tweet, name='d_tweet'),
    path('home/', home_view, name='home'),
    path('hashtags/', hashtags_view, name='hashtags_all'),
    path('hashtags/<str:t_name>/', hashtags_filter, name='hashtags_filtered')
]
