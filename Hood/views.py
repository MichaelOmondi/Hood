# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, PostForm, ProfileForm, CommentForm
from .models import Post, Profile, Comments
from  django.contrib import messages

# Create your views here.

# Login
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/accounts/login')
def index(request):
    posts = Post.get_all_posts()

    return render(request, 'index.html',{'posts':posts})

@login_required(login_url='/accounts/login')
def kampala(request):
    posts = Post.get_all_posts()

    return render(request, 'kampala.html',{'posts':posts})

@login_required(login_url='/accounts/login')
def capetown(request):
    posts = Post.get_all_posts()

    return render(request, 'capetown.html',{'posts':posts})

# Signup
def signup(request):
    if request.user.is_authenticated():
        return redirect('index')
    else:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                to_email = form.cleaned_data.get('email')
                send_activation_email(user, current_site, to_email)
                return HttpResponse('Confirm your email address to complete registration')
        else:
            form = SignupForm()
            return render(request, 'registration/signup.html',{'form':form})


