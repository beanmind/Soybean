# -*- coding: utf-8 -*-

from forms import LoginForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import ProfileForm


def welcome(request):
    return render(request, 'welcome.html')

def login(request):
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request, 'welcome.html')
        else:
            return render(request, 'login.html', {'ban':form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'ban':form})

def register(request):
    if len(request.GET)>0:
        form  =  ProfileForm(request.GET)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/login')
        else:
            return render(request, 'login.html', {'ban':form})
    else:
        form = ProfileForm()
        return render(request, 'user_profile.html', {'ban':form})
