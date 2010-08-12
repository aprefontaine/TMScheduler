from appengine_django.models import BaseModel
from google.appengine.ext import db

# Create your models here.
class Task(db.Model):
    name = db.CharField(max_length=200)
    notes = db.CharField(max_length=200) #TODO this should be a text field
    approver = db.CharField(max_length=200) #TODO this should be the ID of the user not the user's name ForeignKey(User)
    complete_date = db.DateTimeField('date completed')
    start_date = db.DateTimeField('date started')