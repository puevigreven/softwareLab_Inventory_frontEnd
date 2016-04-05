
from __future__ import unicode_literals
from django.db import models
from time import time
class Appointment(models.Model):
	NameOfDoctor = models.CharField(max_length=254)
        DateOfBirth = models.DateField(auto_now=False,auto_now_add=False) 
        Contact = models.IntegerField(default = 0)
        PatientId = models.TextField(max_length=254)
        def __unicode__(self):
           return self.PatientId
          

	
