# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

# Registration/Login Page
def index(request):
    return render(request, 'logreg/index.html')

# Registration/Login Confirmation Page
def success(request):
    return render(request, 'logreg/success.html')

# Process Registration
def regist(request):
    return redirect('/success')

# Verification of login
def login(request):
    return redirect('/success')