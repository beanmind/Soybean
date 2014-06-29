from django.contrib import admin
from mysite.models import people, recipe, quantities, ingredient

admin.site.register(people)
admin.site.register(recipe)
admin.site.register(quantities)
admin.site.register(ingredient)


