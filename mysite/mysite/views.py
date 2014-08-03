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


def addrecipe(request):
    logged_user = get_logged_user_from_request(request)
    print"1"
    if logged_user:
        print"2"
        if "newRecipeTitle" in request.GET and request.GET["newRecipeTitle"]:
            if "newRecipeInstructions" in request.GET and request.GET["newRecipeInstructions"]:
                if "newRecipeIngredients" in request.GET and request.GET["newRecipeIngredients"]:
                    if "newRecipeNPeople" in request.GET and request.GET["newRecipeNPeople"]:
                        print"3"
                        newRecipe = recipe(title=request.GET['newRecipeTitle'],
                                            author=logged_user,
                                            description=request.GET['newRecipeInstructions'],
                                            ingredients=request.GET['newRecipeIngredients'],
                                            number_people=request.GET['newRecipeNPeople'])
                        newRecipe.save()
                        Addedrecipe = recipe.objects.all()
                        print "moi"
                        print Addedrecipe
                        return render(request, 'welcome.html',{'logged_user':logged_user, 'Addedrecipe': Addedrecipe})
                    else:
                        print"4"
                        return render(request, 'addrecipe.html',{'logged_user':logged_user})
               #else:
                #    return render(request, 'welcome.html',{'logged_user':logged_user})
            else:
                print"5"
                return render(request, 'addrecipe.html',{'logged_user':logged_user})
        else:
            print"6"
            return render(request, 'addrecipe.html',{'logged_user':logged_user})
    else:
        print"7"
        return render(request, 'login.html', {'ban':form})

def welcome(request):
    logged_user = get_logged_user_from_request(request)
    Addedrecipe = recipe.objects.all()
    print"ohoho"
    print Addedrecipe
    if logged_user:
        if request.method == "POST":
            return HttpResponseRedirect('/addrecipe')
        elif Addedrecipe.exists():
            print Addedrecipe
            return render(request, 'welcome.html', {'logged_user': logged_user,
                                                   'Addedrecipe': Addedrecipe})
        else:
            return render(request, 'welcome.html',{'logged_user':logged_user, 'Addedrecipe': Addedrecipe})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'ban':form})

def singlerecipe(request):
    logged_user = get_logged_user_from_request(request)
    Addedrecipe = recipe.objects.order_by('title')
    if logged_user:
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
    else:
        form = LoginForm()
        return render(request, 'login.html', {'ban':form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email1']
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
