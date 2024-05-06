from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm
from django.contrib import auth

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Authorization',
        'form': form
    }

    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': 'Registration'
    }

    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Profile'
    }

    return render(request, 'users/profile.html', context)


def logout(request):
    pass