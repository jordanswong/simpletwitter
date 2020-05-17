from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from messaging.models import Tweet
# Create your views here.


def login_view(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/myprofile")
    return render(request, "login.html", {})


def logout_view(request):

    logout(request)
    return redirect("/")


def signup_view(request):

    if request.method == "POST":
        user = User.objects.create_user(username=request.POST['username'],
                                        email=request.POST['email'],
                                        password=request.POST['password'])
        login(request, user)
        return redirect('/myprofile')
    return render(request, "signup.html", {})


def profile_view(request):
    tweets = Tweet.objects.order_by('-created_at')
    return render(request, "myprofile.html", {"tweets": tweets})
