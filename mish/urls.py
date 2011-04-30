from django.conf.urls.defaults import patterns, url
from mish.views import index, del_link

urlpatterns = patterns('',
                       url(r'^$', index),
                       url(r'^del/$', del_link),
                       url(r'^del/(?P<link_id>\d+)$', del_link),
                       )