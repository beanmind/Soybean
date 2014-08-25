# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from mysite.models import recipe



#don't use it!
class LoginForm(forms.Form):
    email1 = forms.EmailField(label='Email:')
    password1 = forms.CharField(label='Password:', widget = forms.PasswordInput)

    def clean(self):
        cleaned_data = super (LoginForm, self).clean()
        email1 = cleaned_data.get("email1")
        password1 = cleaned_data.get("password1")

        if email1 and password1:
            result = people.objects.filter(password=password1, email=email1)
            print result
            print "non"
            if len(result) != 1:

                raise forms.ValidationError("Wrong email or password")
        print cleaned_data
        return cleaned_data

class ProfileForm(UserCreationForm):
    class Meta:
        model= User
        fields = [ "first_name", "last_name", "username"]

#class WelcomeForm(forms.Form):
 #   instructions = forms.CharField(label='Instructions :')
  #  ingredients = forms.CharField(label = 'ingredients')

class AddarecipeForm(ModelForm):
    class Meta:
        model= recipe
        fields = [ "title", "description", "ingredients", "number_people"]