import smtplib, ssl
import math, random
from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from . import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import logout

def generateOTP():
    string = '0123456789'
    OTP = ""
    length = len(string)
    for i in range(6) :
        OTP += string[math.floor(random.random() * length)]
    return OTP

def sendWelcomeMail(receiver_email):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "subhash.prince001@gmail.com"
    password = 'subhash17'
    message = """\
    Subject: Welcome to Amrita Mailroom Service

    Thank you for registering your contact details with Amrita Mailroom Service.
    You will receive E-mail updates on any packages that are sent for you. You
    will receive an OTP with the notification E-mail to verify it's you during the pickup.\
    
    Regards,
    Amrita Mailroom Service."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def sendMail(receiver_email, OTP):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "subhash.prince001@gmail.com"
    password = 'subhash17'
    message = """\
    Subject: Collect Package

    Your package has arrived at the Amrita Mailroom
    Your OTP to collect the package is """ + OTP +'.'

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
def signup(request):
    if request.method == 'POST':
        form = forms.Register(request.POST)
        if form.is_valid():
            form.save()
            sendWelcomeMail(form.cleaned_data.get('Mail_Id'))
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
                generated = generateOTP()
                form.save()
                User_data = models.OtherUsers.objects.all()
                DataToCheck1 = form.cleaned_data.get('RollNo')
                DataToCheck2 = form.cleaned_data.get('Phone')
                for number in User_data:
                    if DataToCheck1 == number.rollNo or DataToCheck2 == number.phone:
                        sendMail(number.Mail_Id, generated)
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
