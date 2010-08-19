from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from tmscheduler.clubs.models import Club 
import datetime

def clubsHome(request):
#    Messages in Django 1.2...
#    club_name = messages.get_messages(request) 
    club_list = Club.objects.all().order_by('Number')
    return render_to_response('clubs/index.html', {'club_list': club_list, 'club_name':club_name})
    
def addClub(request):
    try:
        clubName = request.POST['clubName']
        clubNumber = request.POST['clubNumber']
        clubArea = request.POST['clubArea']
        clubDivision = request.POST['clubDivision']
    except ():
        # 
        return render_to_response('club/index.html', {
            'error_message': "Club create failed.",
        }, context_instance=RequestContext(request))
    else:
        newClub = Club(Name=clubName,Number=clubNumber,Area=clubArea,Division=clubDivision)
        newClub.save()
#        messages.success(request, 'Add') 
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('tmscheduler.clubs.views.clubsHome'))
