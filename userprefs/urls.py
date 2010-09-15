from django.conf.urls.defaults import *
from userprefs.models import UserPrefs

urlpatterns = patterns('',
        (r'^$', 'userprefs.views.index'),
        (r'^update/?$', 'userprefs.views.update'),
)