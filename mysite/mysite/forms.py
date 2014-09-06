# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from mysite.models import recipe

class ProfileForm(UserCreationForm):
    class Meta:
        model= User  # model is a class attribute
        fields = [ "first_name", "last_name", "username"]

class AddarecipeForm(ModelForm):  # AddarecipeForm inherits from (or extends) ModelForm
    class Meta:
        model= recipe
        fields = [ "title", "description", "ingredients", "number_people"]