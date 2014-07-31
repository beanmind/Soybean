
from django.conf.urls import patterns, include
from views import welcome,login, register, addrecipe
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^welcome$', welcome),
    ('^addrecipe$', addrecipe),
    ('^login$', login),
    ('^$', login),
    ('^register$', register),
    ('^admin/', include(admin.site.urls))
)

