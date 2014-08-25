# -*- coding: utf-8 -*-

from forms import AddarecipeForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import ProfileForm
from mysite.models import people, recipe
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


@login_required
def addrecipe(request):
    if request.method == "POST":
        if len(request.POST)>0:
            form=AddarecipeForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/welcome')
            else:
                return render(request, 'addrecipe.html', {'ban':form})
        else:
            return render(request, 'addrecipe.html', {'ban':form})
    else:
        form=AddarecipeForm()
        return render(request, 'addrecipe.html', {'ban':form})


@login_required
def welcome(request):
    Addedrecipe = recipe.objects.all()
    print"ohoho"
    print Addedrecipe

    if request.method == "POST":
        return HttpResponseRedirect('/addrecipe')
    elif Addedrecipe.exists():
        print Addedrecipe
        return render(request, 'welcome.html', {
                                               'Addedrecipe': Addedrecipe})
    else:
        return render(request, 'welcome.html',{ 'Addedrecipe': Addedrecipe})

@login_required
def singlerecipe(request):

    Addedrecipe = recipe.objects.order_by('title')

    if "back_button_singlerecipe" in request.POST:
        return render(request, 'welcome.html',{ 'Addedrecipe': Addedrecipe})
    elif 'RecipeToShow' in request.GET and request.GET['RecipeToShow'] != '':
        results = recipe.objects.filter(id=request.GET['RecipeToShow'])
        print results
        if len(results) == 1:
            recipe_to_show = recipe.objects.get(id=request.GET['RecipeToShow'])
            return render(request, 'single_recipe.html',{'recipe_to_show': recipe_to_show, 'Addedrecipe': Addedrecipe})
        else:
            return render(request, 'single_recipe.html',{'Addedrecipe': Addedrecipe})
    else:
        return render(request, 'single_recipe.html',{'Addedrecipe': Addedrecipe})


@login_required
def searchingredients(request):
    recipe_with_ingredients = recipe.objects.all()
    Addedrecipe = recipe.objects.order_by('title')

    if "back_button_searchingingr" in request.POST:
        return render(request, 'welcome.html',{ 'Addedrecipe': Addedrecipe})
    print "moi et toi"
    #if 'ingredientsSearch' in request.GET and request.GET['ingredientsSearch']:
    list_ingredients = filter(lambda item: len(item.strip()) > 0,request.GET.getlist("ingredientsSearch"))
    print recipe_with_ingredients
    print"hello?"
    print list_ingredients
    if list_ingredients == []:
        print "empty"
        return render(request, 'search_ingredients.html', {'recipe_with_ingredients':[]})
    else:
        for i in list_ingredients:
            print i
            recipe_with_ingredients = recipe_with_ingredients.filter(ingredients__contains= i)
            print recipe_with_ingredients
        return render(request, 'search_ingredients.html', {'recipe_with_ingredients':recipe_with_ingredients})


def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request, user)
            return HttpResponseRedirect('/welcome')

        else:
            print form.errors
            return render(request, 'login.html', {'ban':form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'ban':form})

def register(request):
    if "back_button_register" in request.POST:
        return HttpResponseRedirect('/login')
    elif len(request.POST)>0:
        form=ProfileForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/login')
        else:
            return render(request, 'user_profile.html', {'ban':form})
    else:
        form = ProfileForm()
        return render(request, 'user_profile.html', {'ban':form})

def logout(request):
    logout(request)
    return HttpResponseRedirect('/logout')
