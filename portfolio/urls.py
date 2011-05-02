from django.conf.urls.defaults import patterns
from portfolio.views import view_portfolio

urlpatterns = patterns('',
                       (r'^$', view_portfolio),
                       )
