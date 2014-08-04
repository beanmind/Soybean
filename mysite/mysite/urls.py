
from django.conf.urls import patterns, include
from views import welcome,login, register, addrecipe, singlerecipe, searchingredients
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^welcome$', welcome),
    ('^addrecipe$', addrecipe),
    ('^login$', login),
    ('^$', login),
    ('^register$', register),
    ('^singlerecipe$', singlerecipe),
    ('^searchingredients$', searchingredients),
    ('^admin/', include(admin.site.urls))
)

