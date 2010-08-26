from django.conf.urls.defaults import *
#from django.views.generic.simple import direct_to_template
#from django.views.generic import create_update
#from tasks.models import Task

#tasks_dict = {
#              "model": Task
#    'module_name': 'clubs',
#}

urlpatterns = patterns('',
       # (r'^tasks/$', 'index.html'),
        (r'^$', 'tasks.views.index'),
        (r'^new/$', 'tasks.views.new'),
        (r'^create/$', 'tasks.views.create'),
        (r'^(?P<task_id>\d+)/$', 'tasks.views.show'),
        (r'^edit/(?P<task_id>\d+)/$', 'tasks.views.edit'),
        (r'^update/$', 'tasks.views.update'),
)