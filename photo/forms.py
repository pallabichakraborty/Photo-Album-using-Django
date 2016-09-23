# Code Reference: https://github.com/buckyroberts/Viberr

from django.contrib.auth.models import User
from django import forms
from .models import Photo

# Form to be made available for the user Registration
class UserForm(forms.ModelForm):
    # To make the password not to show up as Cleartext when the user is typing it
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        # Fields for which information to be sorted from the user
        fields = ['username','password']

# Photo Form to be made available
class PhotoForm(forms.ModelForm):
    class Meta:
        model=Photo
        fields=['photo_title', 'photo_caption', 'photo_file','user_id']