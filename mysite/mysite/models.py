from django.db import models
from django.contrib.auth.models import User

class people(models.Model):
    user=models.OneToOneField(User)

    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name

class recipe(models.Model):
    RECIPE_ENTREE = 'E'
    RECIPE_MAIN = 'M'
    RECIPE_DESSERT = 'D'
    RECIPE_BREAD = 'B'
    RECIPE_OTHER = 'O'
    
    RECIPE_TYPE = (
        (RECIPE_ENTREE,'Entree'),
        (RECIPE_MAIN, 'Main course'),
        (RECIPE_DESSERT, 'Dessert'),
        (RECIPE_BREAD, 'Bread'),
        (RECIPE_OTHER, 'Other'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    number_people = models.IntegerField()
    type = models.CharField( max_length=1, choices=RECIPE_TYPE, default='M')
    ingredients = models.TextField()

    def __unicode__(self):
        return self.title
