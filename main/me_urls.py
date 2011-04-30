from django.conf import settings
from main.views import my_route
from accounts.views import my_profile
from django.conf.urls.defaults import patterns, include

urlpatterns = patterns('',
                       (r'^$', my_profile),
                       (r'^portfolio/$', include('portfolio.urls')),
                       (r'^inplaceeditform/', include('inplaceeditform.urls')),
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
                        (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
                       (r'^(?P<url>.*)$', my_route),
                       )
