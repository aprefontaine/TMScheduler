from django.db import models

# Create your models here.

class Club(models.Model):
    # Properties stored in the datastore
    Name = models.CharField(max_length=200)
    Number = models.IntegerField()
    Area = models.IntegerField()
    Division = models.CharField(max_length=20)
    District = models.CharField(max_length=5)
    LastUpdated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.Name