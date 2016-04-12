from __future__ import unicode_literals
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db import models


def validate_Expirydate(value):
	if value <= date.today:
		raise ValidationError(
			_('%(value)s is improper. Medicine has EXPIRED'),
			params={'value': value},
		)


# Create your models here.
class Medicines(models.Model):
	medicine_name = models.CharField(max_length=200)
	expiry_date = models.DateField(default=date.today)
	price = models.PositiveIntegerField(default=0)
	quantity = models.PositiveIntegerField(default=0)
	refill_threshold = models.IntegerField(default=5)
	batch_number = models.TextField(unique=True)
	Issued = models.BooleanField(default=False)
	refill_boolean = models.BooleanField(default=False)

	def __unicode__(self):
		return self.medicine_name

