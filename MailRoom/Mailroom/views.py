import smtplib, ssl
from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from . import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import logout
def sendMail(receiver_email):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "subhash.prince001@gmail.com"
    password = 'subhash17'
    message = """\
    Subject: Collect Package

    Your package has arrived at the Amrita Mailroom
    Your OTP to collect the package is ."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
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
                User_data = models.OtherUsers.objects.all()
                print(User_data)
                DataToCheck = form.cleaned_data.get('RollNo')
                for number in User_data:
                    if DataToCheck == number.rollNo:
                        print(number.Mail_Id)
                        sendMail(number.Mail_Id)
                        print(number.Mail_Id)
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
