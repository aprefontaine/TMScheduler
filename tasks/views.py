# Create your views here.
from google.appengine.ext import db

import django
from django import shortcuts

from tasks.models import Task

def index(request):
  latest_tasks_list = Task.objects.all().order('-pub_date')[:5]
  t = loader.get_template('tasks/index.html')
  c = Context({
    'latest_task_list': latest_tasks_list,
  })
  return HttpResponse(t.render(c))
  
def new(request):
    
    