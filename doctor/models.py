from __future__ import unicode_literals
from django.db import models
from time import time

# Create your models here.

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)


class Patient(models.Model):
	Patient_ID = models.TextField(max_length=254)
	Patient_History = models.TextField()
	Credential = models.FileField(upload_to = get_upload_file_name)
	Doctor_Visited_Id = models.TextField(max_length=254)
	Issued = models.BooleanField(default = False)
    

	def __unicode__(self):
		return self.Patient_ID