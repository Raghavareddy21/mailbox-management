from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from . import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import logout
def signup(request):
    if request.method == 'POST':
        form = forms.Register(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("user saved")
        else:
            return render(request, 'Mailroom/signup.html', {'form': form})
    else:
        form = forms.Register()
    return render(request, 'Mailroom/signup.html', {'form': form})
def Package_entry(request):
    if request.user.is_authenticated:
        form = forms.Package(request.POST)
        if request.method=='POST':
            if form.is_valid():
                form.save()
                return HttpResponse("Package Entered")
            else:
                return render(request, 'Mailroom/entry.html', {'form': form})
        else:
            form=forms.Package()
        return render(request, 'Mailroom/entry.html', {'form': form})
def login(request):
    a
def logout_view(request):
    logout(request)
