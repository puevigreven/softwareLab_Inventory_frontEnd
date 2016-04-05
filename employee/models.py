from __future__ import unicode_literals
from django.db import models
from time import time

# Create your models here.
def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)



class Employee(models.Model):
	Employee_ID = models.TextField(max_length=254)
	Description = models.TextField(max_length=254)
	Credential  = models.FileField(upload_to = get_upload_file_name)


	def __unicode__(self):
		return self.Employee_ID