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

    def save_profile(self):
        self.save()
    
    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile

# comments
class Comments(models.Model):
    comment = HTMLField()
    posted_on = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()
    
    @classmethod
    def get_comments_by_posts(cls, id):
        comments = Comments.objects.filter(post__pk = id)
        return comments

#post
class Post(models.Model):
    photo = ImageField(blank=True, manual_crop='800x800')
    post_name = models.CharField(max_length = 50)
    post_caption = HTMLField(blank=True)
    post_date = models.DateTimeField(auto_now=True)
    likes = models.BooleanField(default=False)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-post_date',)

    def save_post(self):
        self.save()
    
    @classmethod
    def update_caption(cls, update):
        pass
    
    @classmethod
    def get_post_id(cls, id):
        post = Post.objects.get(pk=id)
        return post
    
    @classmethod
    def get_profile_posts(cls, profile):
        posts = Post.objects.filter(profile__pk = profile)
        return posts
    
    @classmethod
    def get_all_posts(cls):
        posts = Post.objects.all()
        return posts        
        


