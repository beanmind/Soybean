#-*- coding: utf-8 -*-

from django import forms
from mysite.models import people

class LoginForm(forms.Form):
    email1 = forms.EmailField(label='Email:')
    password1 = forms.CharField(label='Password:', widget = forms.PasswordInput)
    print email1
    print password1
    def clean(self):
        cleaned_data = super (LoginForm, self).clean()
        email1 = cleaned_data.get("email1")
        password1 = cleaned_data.get("password1")
        if email1 and password1:
            result = people.objects.filter(password=password1, email=email1)
            if len(result) != 1:
                raise forms.ValidationError("Wrong email or password")
            
        return cleaned_data

class ProfileForm(forms.ModelForm):
    class Meta:
        model= people
        