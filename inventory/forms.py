from django import forms
from models import Medicines


class MedicinesForm(forms.ModelForm):

	class Meta:
		model = Medicines
		fields = ('medicine_name', 'expiry_date', 'price', 'quantity','refill_threshold' , 'batch_number')

class QuantityForm(forms.Form):
	medicine_quantity = forms.IntegerField(min_value=0)
