from __future__ import print_function
from django.shortcuts import render_to_response, redirect
from inventory.models import Medicines
from forms import MedicinesForm
from forms import QuantityForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')


def all(request):
	return HttpResponseRedirect('inventory/all_med')


def display_all_medicines(request):
	return render_to_response('all_medicines.html', {'medicines': Medicines.objects.all()})


def display_medicine(request, med_name):
	return render_to_response('medicine.html', {'medicine': Medicines.objects.get(medicine_name=med_name)})

def create(request):
	if request.POST:
		form = MedicinesForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')

	else:
		form = MedicinesForm()

	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('create_medicine.html', args)	


def searchMedicine(request):
	if request.method == 'POST':
		search_text = request.POST['search_text']
	else:
		search_text = ''
		
	medicines = Medicines.objects.filter(medicine_name__contains=search_text)
	return render_to_response('ajax_search.html', {'medicines': medicines})


def issueMedicines(request , med_name):
	if request.POST:
		print('hello')
		form = QuantityForm(request.POST)
		if form.is_valid():
			#form.save()
			medicine = Medicines.objects.get(medicine_name=med_name)
			print (medicine.quantity)
			print (request.POST['medicine_quantity'])

			if medicine.quantity < int(request.POST['medicine_quantity']):
				print ('error in quantity')

			elif (medicine.quantity - 5) < int(request.POST['medicine_quantity']):
				medicine.quantity -= int(request.POST['medicine_quantity'])

				medicine.refill = True
				medicine.save()
				print ('refill on')

			else:
				medicine.quantity -= int(request.POST['medicine_quantity'])
				medicine.save()
				print("updated value : %s" % medicine.quantity)

			return HttpResponseRedirect('/inventory/all_med/')

	else:
		form = MedicinesForm()

	print('hello')

	args = {}
	args.update(csrf(request))
	args['form'] = form
	args['med_name'] = med_name
	return render_to_response('issue_medicine.html', args)


def refillMedicines(request):
	return render_to_response('refillMedicines.html', {'medicines': Medicines.objects.filter(refill=True)})