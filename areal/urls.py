from django.conf.urls.defaults import patterns, url
from areal.views import index

urlpatterns = patterns('',
                       url(r'^$', index),
                       )