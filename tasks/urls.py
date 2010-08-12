from django.conf.urls.defaults import *

urlpatterns = patterns ('',
    (r'new', 'django.views.generic.simple.direct_to_template', {'template': 'new.html'}),
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),
)