
from django.conf.urls import patterns, include
from views import welcome,login, register, addrecipe, singlerecipe
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^welcome$', welcome),
    ('^addrecipe$', addrecipe),
    ('^login$', login),
    ('^$', login),
    ('^register$', register),
    ('^singlerecipe$', singlerecipe),
    ('^admin/', include(admin.site.urls))
)

