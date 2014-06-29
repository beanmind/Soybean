
from django.conf.urls import patterns, include
from views import welcome,login, register
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^welcome$', welcome),
    ('^login$', login),
    ('^$', login),
    ('^register$', register),
    ('^admin/', include(admin.site.urls))
)

