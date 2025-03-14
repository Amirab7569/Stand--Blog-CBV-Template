from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def login_view(request):
    # start to write login code
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
    else:
        return redirect("/")
    return render(request, "account/login.html", {})

def logout_view(request):
    logout(request)
    return redirect("/")


def register_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            re_password = request.POST.get("repassword")
            if password != re_password :
                messages.error(request, "Password and Repassword dosn't match", extra_tags="danger")
            else:
                user = User.objects.create(username=username, password=password ,email=email)
                login(request, user)
                return redirect("/")


    return render(request, "account/register.html")