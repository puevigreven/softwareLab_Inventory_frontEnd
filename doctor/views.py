from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from doctor.models import Patient
from practitioner.models import Practitioner
from django.http import HttpResponse
from forms import PatientForm
from django.contrib.auth.models import User
from appointments.models import Appointment
from practitioner.models import Practitioner
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext

# Create your views here.

def patients(request, doctor_id=1):
	args = {}
	args.update(csrf(request))
	args['doctor'] = doctor_id
	args['patients'] = Patient.objects.filter( Doctor_Visited_Id = doctor_id)
	return render_to_response('patients.html',
		args )


def appointment(request, doctor_id=1):
        args = {}
        args['userid'] = doctor_id
	temp = Practitioner.objects.get(id = doctor_id)
	args['RequiredPatient'] = Appointment.objects.filter(NameOfDoctor = temp.Practitioner_Name)
	return render_to_response('appointment.html', args)


def patient(request, doctor_id=1 , patient_id=1):
	return render_to_response('patient.html', 
		{'patient': Patient.objects.get(id = patient_id), 'practitioner': Practitioner.objects.get(id = doctor_id)})


def create(request, doctor_id=1):
	if request.POST:
		form = PatientForm(request.POST, request.FILES)
		form.instance.Doctor_Visited_Id = doctor_id
		if form.is_valid():
			if User.objects.filter(username = request.POST['Patient_ID']).exists():
				form.save()
				return HttpResponseRedirect('/doctor/%s/all/' % doctor_id)
			else:
				print "Enter valid ID" # CHANGE THIS IN FUTURE FOR ERROR MESSAGE !
			

	else:
		form = PatientForm()

	args = {}
	args.update(csrf(request))
	args['form'] = form
	args['doctor'] = doctor_id
	return render_to_response('create_patient.html', args)	


def search(request, doctor_id=1):
	if request.POST:
		if request.POST['pid'] is not None:
			patients = Patient.objects.filter(Patient_ID__icontains = request.POST['pid'])
		if request.POST['hist'] is not None:
			patients = patients.filter(Patient_History__icontains = request.POST['hist'])
		return render_to_response('search_list.html', {'patients':patients, 'doctor': doctor_id })

	return render_to_response('search.html', {'doctor':doctor_id}, context_instance=RequestContext(request))
