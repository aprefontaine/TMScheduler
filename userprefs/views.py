from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template import Context, loader
from google.appengine.api import users
from userprefs.models import *
from clubs.models import Club
import logging

def index(request):
    user = users.get_current_user()
    club = None
    phone = ""
    if not user:
        auth_url = users.create_login_url(request.path + '/prefs')
    else:
        auth_url = users.create_logout_url(request.path)
        userPrefs = get_userprefs(user.user_id())
        logging.info('userPrefs index: get_userprefs returns %s' % userPrefs)
        if userPrefs:
            logging.info('userPrefs: %s' % (userPrefs,))
            club = userPrefs.club
            phone = userPrefs.phone
        else: 
            # should we ever get here? We should always get a userPref but version of prefs may be 0.
            logging.info('userPrefs: no record yet. Why here??')
    clubList = Club.objects.all().order_by('Number')    
    t = loader.get_template('userprefs/index.html')
    c = RequestContext(request, {
        'user': user,
        'auth_url': auth_url,
        'club': club,
        'phone': phone,
        'clubList' : clubList
    })
    return HttpResponse(t.render(c))

def update(request):
    try:
        user = users.get_current_user()
        clubNumber = request.POST['clubNumber']
        phoneNumber = request.POST['phoneNumber']
    except ():
       # 
        return render_to_response('prefs/index.html', {
            'error_message': "Prefs update failed.",
        }, context_instance=RequestContext(request))
    else:
        logging.info('Save UserPrefs: club=['+clubNumber+'], phoneNumber=['+phoneNumber+'], gid=['+user.user_id()+']')
        newUserPrefs = UserPrefs(version=1,club=clubNumber,phone=phoneNumber,googleOpenId=user.user_id())
        newUserPrefs.save()
#        messages.success(request, 'Add') 
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('userprefs.views.index'))
#        return HttpResponse('Test')