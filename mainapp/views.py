from django.http import HttpResponse
from django.template import RequestContext
from django.template import Context, loader
from google.appengine.api import users

def index(request):
    user = users.get_current_user()
    if not user:
        auth_url = users.create_login_url(request.path + 'prefs/')
    else:
        auth_url = users.create_logout_url(request.path)
    t = loader.get_template('home.html')
    c = RequestContext(request, {
        'user': user,
        'auth_url': auth_url,
    })
    return HttpResponse(t.render(c))