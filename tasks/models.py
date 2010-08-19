from django.db import models
#from google.appengine.ext import db

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    notes = models.CharField(max_length=200) #TODO this should be a text field
    approver = models.CharField(max_length=200) #TODO this should be the ID of the user not the user's name ForeignKey(User)
    #complete_date = models.DateTimeField('date completed')
    #start_date = models.DateTimeField('date started')