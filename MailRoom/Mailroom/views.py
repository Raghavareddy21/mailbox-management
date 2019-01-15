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
            generated = generateOTP()
            print(generated)
            form.instance.OTP=generated
            print(form)
            if form.is_valid():
                form.save()
                #num=models.Package.objects.get(RollNo=form.RollNo)
                #num[0].OTP=generated
                #print(num.OTP)
                User_data = models.OtherUsers.objects.all()
                print(User_data)
                DataToCheck = form.cleaned_data.get('RollNo')
                for number in User_data:
                    if DataToCheck == number.rollNo:
                        print(number.Mail_Id)
                        sendMail(number.Mail_Id, generated)
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
def retrieve(request):
    if request.user.is_authenticated:
        form = forms.Retrieve(request.POST)
        if request.method=='POST':
            if form.is_valid():
                OTP=form.cleaned_data.get('OTP'),
                RollNo=form.cleaned_data.get('RollNo')
                roll=models.Package.objects.all()
                for number in roll:
                    if RollNo==number.RollNo:
                        if OTP== number.OTP:
                            return redirect('verified.html')
    return render(request,'Mailroom/delivery.html',{'form':form})
