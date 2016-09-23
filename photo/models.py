# -*- coding: utf-8 -*-
# Code Reference: https://github.com/buckyroberts/Viberr

from __future__ import unicode_literals
from django.urls import reverse

from django.db import models

#Model/ Data structure for the Photo object
class Photo(models.Model):

    photo_title = models.CharField(max_length=100)
    photo_caption=models.CharField(max_length=100,default=' ')
    photo_file=models.FileField()
    photo_uploadtime=models.DateTimeField(auto_now=True)
    user_id=models.CharField(max_length=30,default='publicuser')

    #This is to make the identification of the Photo Objects easier when seen from the admin panel or through the shell
    def __str__(self):
        return self.photo_title+"-"+self.user_id

    # Generate url patterns which can be used to used to match patterns with incoming URL patterns to be used by the views.
    def get_absolute_url(self):
        return reverse('photo:index')