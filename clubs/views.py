from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from clubs.models import Club 
import datetime

class ClubContextBase:
    Type = 0
    ClubList = []
    
def clubsHome(request):
#    Messages in Django 1.2...
#    club_name = messages.get_messages(request) 
    clubContext = ClubContextBase
    clubContext.ClubList = Club.objects.all().order_by('Number') 
    return render_to_response('clubs/index.html', {'clubContext': clubContext}, context_instance=RequestContext(request))

class ClubContextAdd(ClubContextBase):
    Type = 2
    Success = 0
        
def addClub(request):
    clubContext = ClubContextAdd()
    try:
        clubName = request.POST['clubName']
        clubNumber = request.POST['clubNumber']
        clubArea = request.POST['clubArea']
        clubDivision = request.POST['clubDivision']
        clubDistrict = request.POST['clubDistrict']
    except ():
        # 
        return render_to_response('clubs/index.html', {
            'error_message': "Club create failed.",
        }, context_instance=RequestContext(request))
    else:
        newClub = Club(Name=clubName,Number=clubNumber,Area=clubArea,Division=clubDivision,District=clubDistrict)
        newClub.save()
#        messages.success(request, 'Add') 
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('clubs.views.clubsHome'))

def importClubs(request):
    return render_to_response('clubs/ClubImport.html',
                              {'test': 'I am the second view.'},
                              context_instance=RequestContext(request))

class ClubContextImport(ClubContextBase):
    Type = 1
    Added = 0
    Existing = 0
    Errors = 0

def doImportClubs(request):
    csvText = request.POST['csvClubData']
    lines  = csvText.split('\n')
    clubContext = ClubContextImport()
    for nextLine in lines:
        fields = nextLine.split(',')
        clubName = fields[0]
        clubNum = fields[1]
        clubArea = fields[2]
        clubDiv = fields[3]
        clubDistrict = fields[4]
        existingClub = Club.objects.filter(Number=clubNum)
        if len(existingClub) == 0:
            newClub = Club(Name=clubName,Number=clubNum,Area=clubArea,Division=clubDiv,District=clubDistrict)
            newClub.save()
            clubContext.Added = clubContext.Added + 1
        else:
            clubContext.Existing = clubContext.Existing + 1
    clubContext.ClubList = Club.objects.all().order_by('Number')        
    return render_to_response('clubs/index.html', {'clubContext': clubContext})    
#    return HttpResponseRedirect(reverse('clubs.views.clubsHome'), {'clubContext': clubContext})


    