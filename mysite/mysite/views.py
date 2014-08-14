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
    Addedrecipe = recipe.objects.all()

    if logged_user:
        if "back_button_addrecipe" in request.POST:
            return render(request, 'welcome.html',{'logged_user':logged_user, 'Addedrecipe': Addedrecipe})
        elif "newRecipeTitle" in request.POST and request.POST["newRecipeTitle"]:
            if "newRecipeInstructions" in request.POST and request.POST["newRecipeInstructions"]:
                if "newRecipeIngredients" in request.POST and request.POST["newRecipeIngredients"]:
                    if "newRecipeNPeople" in request.POST and request.POST["newRecipeNPeople"]:
                        print"3"
                        newRecipe = recipe(title=request.POST['newRecipeTitle'],
                                            author=logged_user,
                                            description=request.POST['newRecipeInstructions'],
                                            ingredients=request.POST['newRecipeIngredients'],
                                            number_people=request.POST['newRecipeNPeople'])
                        newRecipe.save()
                        Addedrecipe = recipe.objects.all()

                        print "moi"
                        print Addedrecipe
                        return render(request, 'welcome.html',{'logged_user':logged_user, 'Addedrecipe': Addedrecipe})
                    else:
                        print"4"
                        return render(request, 'addrecipe.html',{'logged_user':logged_user})
                else:
                    return render(request, 'welcome.html',{'logged_user':logged_user})
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
        if "back_button_singlerecipe" in request.POST:
            return render(request, 'welcome.html',{'logged_user':logged_user, 'Addedrecipe': Addedrecipe})
        elif 'RecipeToShow' in request.POST and request.POST['RecipeToShow'] != '':
            results = recipe.objects.filter(id=request.POST['RecipeToShow'])
            print results
            if len(results) == 1:
                recipe_to_show = recipe.objects.get(id=request.POST['RecipeToShow'])
                return render(request, 'single_recipe.html',{'recipe_to_show': recipe_to_show, 'Addedrecipe': Addedrecipe})
            else:
                return render(request, 'single_recipe.html',{'Addedrecipe': Addedrecipe})
        else:
            return render(request, 'single_recipe.html',{'Addedrecipe': Addedrecipe})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'ban':form})

def searchingredients(request):

    logged_user = get_logged_user_from_request(request)
    recipe_with_ingredients = recipe.objects.all()
    Addedrecipe = recipe.objects.order_by('title')
    if logged_user:
        if "back_button_searchingingr" in request.POST:
            return render(request, 'welcome.html',{'logged_user':logged_user, 'Addedrecipe': Addedrecipe})
        print "moi et toi"
        #if 'ingredientsSearch' in request.GET and request.GET['ingredientsSearch']:
        list_ingredients = request.GET.getlist("ingredientsSearch")
        print"hello?"
        print list_ingredients
        for i in list_ingredients:
            print i
            recipe_with_ingredients = recipe_with_ingredients.filter(ingredients__contains= i)
            print recipe_with_ingredients
        return render(request, 'search_ingredients.html', {'recipe_with_ingredients':recipe_with_ingredients})



               # recipe_with_ingredients =



               #print recipe_with_ingredients
               #if len(recipe_with_ingredients) > 0:
                 #  print "yeah"
        #return render(request, 'search_ingredients.html')
        #else:
         #   return render(request, 'search_ingredients.html')
          # else:
           #    return render(request, 'search_ingredients.html')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'ban':form})

def login(request):
    if "submit_login_button" in request.POST:
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
    elif "create_account_login_button" in request.POST:
        return HttpResponseRedirect('/register')
    else:
        form = LoginForm()
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

