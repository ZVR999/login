# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date, datetime
today = date.today()
import re
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First Name must be at least 2 characters'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last Name must be at least 2 characters'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Email is not Valid'
        if postData['dob']:
            if datetime.strptime(postData['dob'], '%Y-%m-%d') > datetime.strptime(str(today), '%Y-%m-%d'):
                errors['dob'] = 'Date of Birth is not Valid'
        else:
            errors['dob'] = 'Please select a Date of Birth'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = 'Password does not match Confirm Password'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=12)
    password = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = UserManager()