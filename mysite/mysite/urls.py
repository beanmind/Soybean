
from django.conf.urls import patterns, include, url
from views import welcome,userlogin, register, addrecipe, singlerecipe, searchingredients, logout
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^welcome$', welcome, name='welcome'),
    url('^addrecipe$', addrecipe, name='addrecipe'),
    url('^login$', userlogin, name='userlogin'),
    url('^$', userlogin, name='userlogin'),
    url('^register$', register, name='register'),
    url('^singlerecipe$', singlerecipe, name='singlerecipe'),
    url('^searchingredients$', searchingredients, name='searchingredients'),
    url('^logout$', logout, name='logout'),
    ('^admin/', include(admin.site.urls))
)

