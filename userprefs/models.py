from django.db import models
from google.appengine.api import users
from clubs.models import Club
import logging
# Create your models here.

#
# User Preferences. Linked to a Google ID.
# We'll maintain a version of the preferences data currently saved on disk so that we can
# upgrade data later if we add preferences.
# Version will equal 0 if the user has never saved preferences.
#
class UserPrefs(models.Model):
    version = models.IntegerField(default=0)
    club = models.IntegerField(default=0)
    phone = models.CharField(max_length=20)
    googleOpenId = models.CharField(max_length=50)
    
#
# Returns : None - No one is curently logged in
#         : UserPrefs object - a user is currently logged in. googleOpenId will be set to the Google user
#                              of the logged in user. The other preferences will be defaulted if the
#                              user has never updated preferences.
def get_userprefs(user_id=None):
    if not user_id:
        user = users.get_current_user()
        if not user:
            return None
        user_id = user.user_id()
    logging.info("get_userprefs: for uid=%s" % (user_id, ))    
    userprefs = UserPrefs.objects.filter(googleOpenId=user_id)
    if userprefs.count() == 1:
        logging.info('get_userprefs: Found record! %s' % (userprefs,))
        return userprefs[0]
    else:
        logging.info('get_userprefs: Not Found!')    
        userprefs = UserPrefs(googleOpenId=user_id)
        return userprefs
