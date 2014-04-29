
from django.conf.urls import patterns
from views import welcome,login

urlpatterns = patterns('',
    ('^welcome$',welcome),
    ('^login$', login),
    ('^$', login),
    
)
  