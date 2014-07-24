# -*- coding: utf-8 -*-

from forms import LoginForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import ProfileForm
from mysite.models import people


def welcome(request):
    print "bla"
    print 
    print "moi"
    if 'logged_user_id' in request.session:
        print logged_user_id
        logged_user_id = request.session['logger_user_id']
        logged_user = people.objects.get(id = logged_user_id)
        print logged_user
        return render(request, 'welcome.html',{'logged_user':logged_user})
    else:
        return render(request, 'login.html', {'ban':form})
           
def login(request):
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email1']
            print user_email
            logged_user = people.objects.get(email=user_email)
            print logged_user
            request.session['logged_user_id'] = logged_user.id
            print logged_user.id
            print logged_user.name            
            return render(request, 'welcome.html',{'logged_user':logged_user}) 
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
