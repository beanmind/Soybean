# -*- coding: utf-8 -*-

from forms import LoginForm
from django.shortcuts import render

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
    