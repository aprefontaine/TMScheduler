from django.conf.urls.defaults import *

urlpatterns = patterns('',
    ('^$', 'mainapp.views.index'),
    (r'^tasks/', include('tasks.urls')),
    (r'^clubs/', include('clubs.urls')),
    (r'^prefs/', include('userprefs.urls')),
)
