from django.conf.urls.defaults import patterns
from blog.views import blog_index

urlpatterns = patterns('',
                       (r'^$', blog_index),
                       )
