from django.db import models

class people(models.Model):
    identifier = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    password = models.CharField(max_length=32)
    email = models.EmailField()

    def __unicode__(self):
        return self.name + " " + self.surname

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
    author = models.ForeignKey(people)
    date_of_publication = models.DateField()
    description = models.TextField()
    number_people = models.IntegerField()
    type   = models.CharField( max_length=1, choices=RECIPE_TYPE, default='M')    
    
    def __unicode__(self):
        return self.title
        
class quantities(models.Model):
    quantity = models.CharField(max_length=30) 
    
    def __unicode__(self):
        return self.quantity
     
class ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.ManyToManyField(quantities)
    use = models.ManyToManyField(recipe)
    def __unicode__(self):
        return self.name
