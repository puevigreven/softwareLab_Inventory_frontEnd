from django import forms
from models import Employee


class EmplyoeeForm(forms.ModelForm):

	class Meta:
		model = Employee
		fields = ('Credential','Employee_ID','Description')