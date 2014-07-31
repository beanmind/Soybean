# -*- coding: utf-8 -*-

from forms import LoginForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import ProfileForm
from mysite.models import people, recipe

def get_logged_user_from_request(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        if len(people.objects.filter(id=logged_user_id)) == 1:
            return people.objects.get(id=logged_user_id)
        else:
            return None
    else:
        return None


def welcome(request):
    logged_user = get_logged_user_from_request(request)
    if logged_user:
        if "newRecipeTitle" in request.GET and request.GET["newRecipeTitle"]:
            if "newRecipeInstructions" in request.GET and request.GET["newRecipeInstructions"]:
               #if "newRecipeIngredients" in request.GET and request.GET["newRecipeIngredients"]:
                    if "newRecipeNPeople" in request.GET and request.GET["newRecipeNPeople"]:
                        newRecipe = recipe(title=request.GET['newRecipeTitle'],
                                            author=logged_user,
                                            description=request.GET['newRecipeInstructions'],
                                           # ingredients=request.GET['newRecipeIngredients'],
                                            number_people=request.GET['newRecipeNPeople'])
                        newRecipe.save()
                        return render(request, 'welcome.html',{'logged_user':logged_user,'newRecipe':newRecipe})
                    else:
                        return render(request, 'welcome.html',{'logged_user':logged_user})
               #else:
                #    return render(request, 'welcome.html',{'logged_user':logged_user})
            else:
                return render(request, 'welcome.html',{'logged_user':logged_user})
        else:
            return render(request, 'welcome.html',{'logged_user':logged_user})
    else:
        return render(request, 'login.html', {'ban':form})
        
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email1']
            print "yeah"
            print user_email
            logged_user = people.objects.get(email=user_email)
            print logged_user
            request.session['logged_user_id'] = logged_user.id
            print logged_user.id
            print logged_user.name
            return HttpResponseRedirect('/welcome')
        else:
            return render(request, 'login.html', {'ban':form})

    else:
        form = LoginForm()
        return render(request, 'login.html', {'ban':form})

def register(request):
    if len(request.GET)>0:
        form=ProfileForm(request.GET)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/login')
        else:
            return render(request, 'login.html', {'ban':form})
    else:
        form = ProfileForm()
        return render(request, 'user_profile.html', {'ban':form})
