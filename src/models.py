
from google.appengine.api import memcache
from google.appengine.api import users
from google.appengine.ext import db
import logging

class UserPrefs(db.Model):
    tz_offset = db.IntegerProperty(default=0)
    user = db.UserProperty(auto_current_user_add=True)
    
    def cache_set(self):
        logging.info('UserPrefs : cache set')
        memcache.set(self.key().name(), self, namespace=self.key().kind())
        
    def put(self):
        self.cache_set()
        db.Model.put(self)
    
def get_userprefs(user_id=None):
    if not user_id:
        user = users.get_current_user()
        if not user:
            logging.info('get_userprefs : user not found')
            return None
        user_id = user.user_id()
        logging.info('get_userprefs : got user_id of ' + user_id)
    
    userprefs = memcache.get(user_id, namespace='UserPrefs')    
    if not userprefs:
        logging.info('get_userprefs : user not in cache')
        key = db.Key.from_path('UserPrefs', user_id)
        userprefs = db.get(key)
        if userprefs:
            logging.info('get_userprefs : user found in DB')
            userprefs.cache_set()
        else:
            logging.info('get_userprefs : create new UserPrefs obj')
            userprefs = UserPrefs(key_name=user_id)

    return userprefs

