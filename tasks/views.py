# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
#from google.appengine.ext import db

import django
from django import shortcuts

from .models import Task
#from tasks.models import Task

def index(request):
    task_list = Task.objects.all()
    return render_to_response('tasks/index.html', {'task_list': task_list})
#    return render_to_response('tasks/index.html')
    #return HttpResponse("Hello, world. You're at the poll index.")
  
def new(request):
#    new_task = Task.objects.new
#    t = loader.get_template('tasks/index.html')
#    c = Context({
#                 'new_task': new_task,
#                 })
#    return HttpResponse(t.render(c))
    return render_to_response('tasks/new.html')

def create(request):
    if request.POST:
        try:
            task_name = request.POST['task_name']
        
        except ():
            # 
            return render_to_response('tasks/index.html', {
                'error_message': "Task create failed.",
            }, context_instance=RequestContext(request))
        else:
            newTask = Task(name=task_name)
            newTask.save()
    #        messages.success(request, 'Add') 
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            #return HttpResponseRedirect('tmscheduler_norel.tasks.views.index')
            return render_to_response('tasks/index.html')
            
        
        #return HttpResponse("Hello, world. You're at the poll index." + task_name)
        #return HttpResponseRedirect('tasks/index.html')
    
    
    