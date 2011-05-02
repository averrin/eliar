from django.conf import settings
from main.views import my_route
from django.conf.urls.defaults import patterns, include
from blog.views import blog_index

urlpatterns = patterns('',
                       (r'^$', blog_index),
                       (r'^blog/$', include('blog.urls')),
                        (r'^inplaceeditform/', include('inplaceeditform.urls')),
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
                        (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
                       (r'^(?P<url>.*)$', my_route),
                       )
