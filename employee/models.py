from __future__ import unicode_literals
from django.db import models
from time import time

# Create your models here.
def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)



class Employee(models.Model):
	Patient_ID = models.TextField(max_length=254)
	Description = models.TextField(max_length=254)
	Date_Of_Upload = models.DateField(auto_now=False,auto_now_add=False) 
	Credential  = models.FileField(upload_to = get_upload_file_name)


	def __unicode__(self):
		return self.Patient_ID


class Schedule(models.Model):
	r00 = models.CharField(max_length=254)	
	r01 = models.CharField(max_length=254)
	r02 = models.CharField(max_length=254)
	r03 = models.CharField(max_length=254)
	r04 = models.CharField(max_length=254)
	r05 = models.CharField(max_length=254)
	r06 = models.CharField(max_length=254)
	r10 = models.CharField(max_length=254)
	r11 = models.CharField(max_length=254)
	r12 = models.CharField(max_length=254)
	r13 = models.CharField(max_length=254)
	r14 = models.CharField(max_length=254)
	r15 = models.CharField(max_length=254)
	r16 = models.CharField(max_length=254)
	r20 = models.CharField(max_length=254)
	r21 = models.CharField(max_length=254)
	r22 = models.CharField(max_length=254)
	r23 = models.CharField(max_length=254)
	r24 = models.CharField(max_length=254)
	r25 = models.CharField(max_length=254)
	r26 = models.CharField(max_length=254)
	r30 = models.CharField(max_length=254)
	r31 = models.CharField(max_length=254)
	r32 = models.CharField(max_length=254)
	r33 = models.CharField(max_length=254)
	r34 = models.CharField(max_length=254)
	r35 = models.CharField(max_length=254)
	r36 = models.CharField(max_length=254)
	r40 = models.CharField(max_length=254)
	r41 = models.CharField(max_length=254)
	r42 = models.CharField(max_length=254)
	r43 = models.CharField(max_length=254)
	r44 = models.CharField(max_length=254)
	r45 = models.CharField(max_length=254)
	r46 = models.CharField(max_length=254)
	r50 = models.CharField(max_length=254)
	r51 = models.CharField(max_length=254)
	r52 = models.CharField(max_length=254)
	r53 = models.CharField(max_length=254)
	r54 = models.CharField(max_length=254)
	r55 = models.CharField(max_length=254)
	r56 = models.CharField(max_length=254)
	
	def __unicode__(self):
		return self.r01