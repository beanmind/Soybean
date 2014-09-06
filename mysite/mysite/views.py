# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from forms import AddarecipeForm, ProfileForm
from models import recipe

# page to add a new recipe (title, instructions, ingredients, number of people)
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
            form=AddarecipeForm()
            return render(request, 'addrecipe.html', {'ban':form})
    else:
        form=AddarecipeForm()
        return render(request, 'addrecipe.html', {'ban':form})

# Homepage. One can click on an existing recipe, add a new recipe, search for a recipe containing specific ingredients, log out
@login_required
def welcome(request):
    Addedrecipe = recipe.objects.all()
    if request.method == "POST":
        return HttpResponseRedirect('/addrecipe')
    elif Addedrecipe.exists():
        return render(request, 'welcome.html', {'Addedrecipe': Addedrecipe})
    else:
        return render(request, 'welcome.html')

# page displaying an existing recipe
@login_required
def singlerecipe(request):
    Addedrecipe = recipe.objects.all()
    if 'RecipeToShow' in request.GET and request.GET['RecipeToShow'] != '':
        results = recipe.objects.filter(id=request.GET['RecipeToShow'])
        print results
        if len(results) == 1:
            recipe_to_show = recipe.objects.get(id=request.GET['RecipeToShow'])
            return render(request, 'single_recipe.html',{'recipe_to_show': recipe_to_show, 'Addedrecipe': Addedrecipe})
        else:
            return render(request, 'single_recipe.html',{'Addedrecipe': Addedrecipe})
    else:
        return render(request, 'single_recipe.html',{'Addedrecipe': Addedrecipe})

# page for searching for a recipe containing specific ingredients. Up to 5 ingredients can be entered.
@login_required
def searchingredients(request):
    recipe_with_ingredients = recipe.objects.all()
    list_ingredients = filter(lambda item: len(item.strip()) > 0,request.GET.getlist("ingredientsSearch"))
    if list_ingredients == []:
        return render(request, 'search_ingredients.html', {'recipe_with_ingredients':[]})
    else:
        for i in list_ingredients:
            recipe_with_ingredients = recipe_with_ingredients.filter(ingredients__contains= i)
        return render(request, 'search_ingredients.html', {'recipe_with_ingredients':recipe_with_ingredients})

# Login page
def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return HttpResponseRedirect('/welcome')
        else:
            print form.errors
            return render(request, 'login.html', {'ban':form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'ban':form})

# page to register
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

# logout page
def logout(request):
    return render(request,'logout.html')
