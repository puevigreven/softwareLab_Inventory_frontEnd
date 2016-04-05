from __future__ import unicode_literals
from django.db import models
from time import time

# Create your models here.

class Pharma(models.Model):
	Pharma_ID = models.TextField(max_length=254)
	Pharma_Name = models.TextField(max_length=254)
	Date_Of_Joining = models.DateField()
	User_ID = models.TextField(max_length=254)
	Password = models.TextField(max_length=254)

	def __unicode__(self):
		return self.Pharma_ID