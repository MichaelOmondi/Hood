# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField


# Create your models here.
# Profile
class Profile(models.Model):
    prof_pic = ImageField(blank=True, manual_crop='800x800')
    bio = HTMLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    
