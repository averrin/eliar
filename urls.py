from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from main.views import *
from accounts.views import *
from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout, logout_then_login
from django.views.generic.simple import direct_to_template
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^main/$', index,name='index'),
    url(r'^main/', include('main.urls')),
    url(r'^$', frontend),
    url(r'^about$', direct_to_template ,{'template':'about.html'}, name='about'),
    # Example:
    # (r'^Venona/', include('Venona.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    (r'^admin-media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.ADMIN_MEDIA_ROOT}),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^accounts/login/$', login),
    (r'^accounts/request_invite/$', request_invite),
    (r'^accounts/request_invite/complete$', request_invite_complete),
	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': settings.LOGIN_REDIRECT_URL},name='logout'),
    (r'^accounts/', include('my_invitation.urls')),
    (r'^registration/', include('registration.urls')),
    (r'^dev/', include('dev_tools.urls')),
    (r'^messages/', include('messages.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^rosetta/', include('rosetta.urls')),
    (r'^inplaceeditform/', include('inplaceeditform.urls')),

    url(r'^accounts/profile/(?P<user_id>\d+)$', view_profile,name='profile'),
    (r'^portfolio/$', include('portfolio.urls')),
    (r'^blog/$', include('blog.urls')),
    (r'^mish/', include('mish.urls')),
	(r'^areal/', include('areal.urls')),
)
