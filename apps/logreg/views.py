# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
from datetime import date, datetime
import bcrypt
today = date.today()
# Create your views here.

# Registration/Login Page


def index(request):
    return render(request, 'logreg/index.html')

# Registration/Login Confirmation Page


def success(request):
    return render(request, 'logreg/success.html')

# Process Registration


def regist(request):
    errors = User.objects.basic_validator(request.POST)
    # print len(errors)
    # print errors
    hashed_pw = bcrypt.hashpw(
        request.POST['password'].encode(), bcrypt.gensalt())
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        # print request.POST['dob']
        # print today
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        dob = request.POST['dob']
        User.objects.create(first_name=first_name, last_name=last_name,
                            email=email, date_of_birth=dob, password=hashed_pw)
        

        return redirect('/success')

# Verification of login


def login(request):
    # print bcrypt.checkpw(str(request.POST['password']), hashed_pw.encode())
    return redirect('/success')
