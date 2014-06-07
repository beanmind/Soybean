
from django.conf.urls import patterns, include
from views import welcome,login
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    ('^welcome$',welcome),
    ('^login$', login),
    ('^$', login),
    ('^admin/', include(admin.site.urls))
    
)
  