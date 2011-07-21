from django.conf.urls.defaults import patterns, url
from areal.views import index, get_content

urlpatterns = patterns('',
                       url(r'^$', index),
                       url(r'^getcontent/(?P<msg_id>\d+)$', get_content),
                       )