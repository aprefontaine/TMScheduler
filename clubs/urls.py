from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
#from django.views.generic import create_update
from clubs.models import Club

clubs_dict = {
              "model": Club
#    'module_name': 'clubs',
}

urlpatterns = patterns('',
        (r'^$', 'tmscheduler.clubs.views.clubsHome'),
        (r'^create/?$', 'django.views.generic.create_update.create_object', dict(clubs_dict,post_save_redirect="/club/" ) ),
        (r'^update/(?P<object_id>\d+)/?$', 'django.views.generic.create_update.update_object', clubs_dict),
        (r'^delete/(?P<object_id>\d+)/?$', 'django.views.generic.create_update.delete_object', dict(clubs_dict, post_delete_redirect="/clubs/new/") ),
        (r'^add/?$', 'tmscheduler.clubs.views.addClub' ),
)