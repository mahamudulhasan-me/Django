from dataclasses import fields
from django import forms
from . import models
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=(forms.PasswordInput))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ('facebook_id', 'profile_pic')