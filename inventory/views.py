from __future__ import print_function
from django.shortcuts import render_to_response, redirect
from inventory.models import Medicines
from forms import MedicinesForm
from forms import QuantityForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render
from doctor.models import Patient

glo_patient_id = 0
prescibed_array = []

def home(request):
	return render(request, 'home.html')


def all(request):
	return HttpResponseRedirect('inventory/all_med')


def display_all_medicines(request):
	args = {}
	args.update(csrf(request))
	args['medicines'] = Medicines.objects.filter(quantity__gt=0)
	return render_to_response('all_medicines.html',args)


def display_medicine(request, batch_num):
	return render_to_response('medicine.html', {'medicine': Medicines.objects.get(batch_number=batch_num)})

def create(request):
	if request.POST:
		for med_del in Medicines.objects.filter(refill_boolean=True):
			# print(med_del.medicine_name)
			quantity_sum = 0
			limit = 0
			medicines = Medicines.objects.filter(medicine_name=med_del.medicine_name)
			for medicine_new in medicines:

				quantity_sum += medicine_new.quantity
				if limit < medicine_new.refill_threshold:
					limit = medicine_new.refill_threshold
			# print('medicine name', medicine_new.medicine_name , quantity_sum , limit )
			if quantity_sum > limit:
				medicines_delete = Medicines.objects.filter(medicine_name=med_del.medicine_name, quantity=0)
				for medic in medicines_delete:
					print(medic.medicine_name)
					medic.delete()
				print('deleted')
				med_del.refill_boolean = False
			# med_del.save()

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

	print (glo_patient_id)
	args = {}
	args['patient'] = Patient.objects.get(id=glo_patient_id)
	args['medicines'] = Medicines.objects.filter(medicine_name__contains=search_text)
	return render_to_response('ajax_search.html', args)


def issueMedicines(request , batch_num):
	if request.POST:
		print('hello')
		form = QuantityForm(request.POST)
		if form.is_valid():
			#form.save()
			medicine = Medicines.objects.get(batch_number=batch_num)
			print (medicine.quantity)
			print (request.POST['medicine_quantity'])

			if medicine.quantity < int(request.POST['medicine_quantity']):
				print ('error in quantity')


			elif medicine.quantity == int(request.POST['medicine_quantity']):
				medicine.quantity = 0
				medicine.refill_boolean = True
				medicine.save()
				quantity_sum=0
				medicines = Medicines.objects.filter(medicine_name=medicine.medicine_name)
				for medicine_new in medicines:
					quantity_sum += medicine_new.quantity
				if quantity_sum > 0:
					medicine.delete()
					print('deleted')
					return HttpResponseRedirect('/inventory/')
				else:
					return HttpResponseRedirect('/inventory/')




			elif (medicine.quantity) > int(request.POST['medicine_quantity']):

				if (medicine.quantity - medicine.refill_threshold) <= int(request.POST['medicine_quantity']):
					medicine.quantity -= int(request.POST['medicine_quantity'])
					medicine.refill = True
					medicine.save()
					print('refill on')
					return HttpResponseRedirect('/inventory/')

				else:
					medicine.quantity -= int(request.POST['medicine_quantity'])
					medicine.save()
					print("updated value : %s" % medicine.quantity)
					return HttpResponseRedirect('/inventory/')

	else:
		form = MedicinesForm()

	print('hello')

	args = {}
	args.update(csrf(request))
	args['form'] = form
	args['batch_num'] = batch_num
	return render_to_response('issue_medicine.html', args)


def refillMedicines(request):


	for med in Medicines.objects.all():
		if med.quantity < med.refill_threshold:
			med.refill_boolean = True
			med.save()

	for med_del in Medicines.objects.filter(refill_boolean=True):
		#print(med_del.medicine_name)
		quantity_sum = 0
		limit = 0
		medicines = Medicines.objects.filter(medicine_name=med_del.medicine_name)
		for medicine_new in medicines:

			quantity_sum += medicine_new.quantity
			if limit < medicine_new.refill_threshold:
				limit = medicine_new.refill_threshold
		#print('medicine name', medicine_new.medicine_name , quantity_sum , limit )
		if quantity_sum > limit:
			medicines_delete = Medicines.objects.filter(medicine_name=med_del.medicine_name, quantity=0)
			for medic in medicines_delete:
				print(medic.medicine_name)
				medic.delete()
			print('deleted')
			med_del.refill_boolean = False
			#med_del.save()


	return render_to_response('refillMedicines.html', {'medicines': Medicines.objects.filter(refill_boolean=True)})


def outGoingPatients(request):
	return render_to_response('outgoingpatients.html', {'patients': Patient.objects.filter(Issued=False)})


def get_patients(request, patient_id):
	global glo_patient_id
	glo_patient_id = patient_id
	args = {}
	args.update(csrf(request))
	args['patient'] = Patient.objects.get(id=patient_id)
	args['medicines'] = Medicines.objects.filter(quantity__gt=0)
	return render_to_response('allPatients.html', args)

def issue_Medicines_Patient(request , patient_id):
	#glo_patient_id = patient_id
	args = {}
	args.update(csrf(request))
	args['patient'] = Patient.objects.get(id=patient_id)
	args['medicines'] = Medicines.objects.filter(quantity__gt=0)
	return render_to_response('issue_to_patient.html',args)

def get_Medicines_Patient(request ,patient_id, batch_num ):
	args = {}
	args['patient'] = Patient.objects.get(id=patient_id)
	args['medicine'] = Medicines.objects.get(batch_number=batch_num)
	return render_to_response('get_medicine_to_issue.html',args)

def issueMedicines_toPatients(request ,patient_id, batch_num ):
	if request.POST:
		print('hello')
		args1 = {}
		args1.update(csrf(request))
		args1['patient'] = Patient.objects.get(id=patient_id)
		args1['medicines'] = Medicines.objects.filter(quantity__gt=0)
		args1['arr'] = prescibed_array
		print (prescibed_array)
		form = QuantityForm(request.POST)
		if form.is_valid():
			# form.save()
			medicine = Medicines.objects.get(batch_number=batch_num)
			print(medicine.quantity)
			print(request.POST['medicine_quantity'])

			if medicine.quantity < int(request.POST['medicine_quantity']):
				print('error in quantity')


			elif medicine.quantity == int(request.POST['medicine_quantity']):
				prescibed_array.append(medicine.medicine_name)
				medicine.quantity = 0
				medicine.refill_boolean = True
				medicine.save()
				quantity_sum = 0
				medicines = Medicines.objects.filter(medicine_name=medicine.medicine_name)
				for medicine_new in medicines:
					quantity_sum += medicine_new.quantity
				if quantity_sum > 0:
					medicine.delete()
					print('deleted')
					return render_to_response('allPatients.html', args1)
				else:
					return render_to_response('allPatients.html', args1)




			elif (medicine.quantity) > int(request.POST['medicine_quantity']):
				prescibed_array.append(medicine.medicine_name)
				if (medicine.quantity - medicine.refill_threshold) <= int(request.POST['medicine_quantity']):
					medicine.quantity -= int(request.POST['medicine_quantity'])
					medicine.refill = True
					medicine.save()
					print('refill on')
					return render_to_response('allPatients.html', args1)

				else:
					medicine.quantity -= int(request.POST['medicine_quantity'])
					medicine.save()
					print("updated value : %s" % medicine.quantity)
					return render_to_response('allPatients.html', args1)

	else:
		form = MedicinesForm()

	print('hello')

	args = {}
	args.update(csrf(request))
	args['form'] = form
	args['batch_num'] = batch_num
	args['patient'] = Patient.objects.get(id=patient_id)
	return render_to_response('issue_medicine.html', args)
