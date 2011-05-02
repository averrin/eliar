from django.conf.urls.defaults import patterns, url
from dev_tools.views import todo_add, todo_del, todo_done

urlpatterns = patterns('',
                       url(r'^todo/add$', todo_add),
                       url(r'^todo/del/(?P<todo_id>\d+)$', todo_del),
                       url(r'^todo/done/(?P<todo_id>\d+)$', todo_done),
                       )
