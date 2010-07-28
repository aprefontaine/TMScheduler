#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import datetime
import models

class MainPage(webapp.RequestHandler):
    def get(self):
        time = datetime.datetime.now()
        user = users.get_current_user()
        if not user:
            navbar = ('<p>Welcome! <a href="%s">Sign in or register</a> to customize.</p>'
                      % (users.create_login_url(self.request.uri)))
            tz_form = ''
        else:
            userprefs = models.get_userprefs()
            navbar = ('<p>Welcome, %s! You can <a href="%s">sign out</a>.</p>'
                      % (user.nickname(), users.create_logout_url(self.request.path)))
            tz_form = '''
                <form action="/prefs" method="post">
                    <label for="tz_offset">
                        Timezone offset from UTC (can be negative):
                    </label>
                    <input name="tz_offset" id="tz_offset" type="text"
                        size="4" value="%d" />
                    <input type="submit" value="Set" />
                </form>
            ''' % userprefs.tz_offset
            time += datetime.timedelta(0,0,0,0,0, userprefs.tz_offset)
            
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('''
        <html>
            <head>
                <title>The Time is ...</title>
            </head>
            <body>
            %s
                <p>Time time is: %s</p>
            %s
            </body>
        </html>
        ''' % (navbar, str(time), tz_form))
            
application = webapp.WSGIApplication([('/', MainPage)],
                                         debug=True)

def main():
    run_wsgi_app(application)


if __name__ == '__main__':
    main()
