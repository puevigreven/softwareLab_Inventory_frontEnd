from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.
class Medicines(models.Model):
	medicine_name = models.CharField(max_length=200)
	expiry_date = models.DateTimeField(default=datetime.now, blank=True)
	price = models.IntegerField(default=0)
	quantity = models.IntegerField(default=0)
	refill = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.medicine_name
