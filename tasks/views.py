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

def show(request,task_id):
    
    task = get_object_or_404(Task, pk=task_id)
    #return HttpResponse("You're looking at the results of poll %s." % task_id)
    return render_to_response('tasks/show.html', {'task': task})

def edit(request,task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render_to_response('tasks/edit.html', {'task': task})
    #return HttpResponse("You're looking at the results of poll %s." % task_id)
    
def update(request):
    task_id = request.POST['task_id']
    task = Task.objects.get(pk=task_id)
    task.name = request.POST['task_name']
    task.notes = request.POST['task_notes']
    task.save()
    return HttpResponseRedirect('/tasks/%d'%task.id)

def create(request):
    if request.POST:
        try:
            task_name = request.POST['task_name']
            task_notes = request.POST['task_notes']
        except ():
            # 
            return render_to_response('tasks/index.html', {
                'error_message': "Task create failed.",
            }, context_instance=RequestContext(request))
        else:
            newTask = Task(name=task_name,notes=task_notes)
            newTask.save()
    #        messages.success(request, 'Add') 
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            #return HttpResponseRedirect('tmscheduler_norel.tasks.views.index')
            return HttpResponseRedirect('/tasks/%d'%newTask.id)
            
        
        #return HttpResponse("Hello, world. You're at the poll index." + task_name)
        #return HttpResponseRedirect('tasks/index.html')
    
    
    