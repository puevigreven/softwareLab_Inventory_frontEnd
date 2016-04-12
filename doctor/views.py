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
import datetime
from employee.models import Employee

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
	temp = Patient.objects.get(id = patient_id)
	args = {}
	args['patient'] = Patient.objects.get(id = patient_id)
	args['practitioner'] = Practitioner.objects.get(id = doctor_id)
	new_temp = temp.Patient_ID
	args['dates'] = Employee.objects.filter(Patient_ID = new_temp)
	return render_to_response('patient.html', args)

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
		patients = Patient.objects.all()
		if request.POST['pid'] !='':
			patients = Patient.objects.filter(Patient_ID__icontains = request.POST['pid'])
		if request.POST['hist'] !='':
			patients = patients.filter(Patient_History__icontains = request.POST['hist'])
		if request.POST['age'] !='':
			year = datetime.date.today().year
			month = datetime.date.today().month
			day = datetime.date.today().day
			temp = int(year) - int(request.POST['age'])
			for patient in patients:
				print patient.Patient_ID+"\n"
				user = User.objects.get(username = patient.Patient_ID)
				search_date = datetime.datetime.strptime(str(temp)+"/"+str(month)+"/"+str(day), "%Y/%m/%d").date()
				print str(search_date)+"\t"+str(user.date_joined.date())+"\n" 
				if user.date_joined.date() < search_date:
					patients = patients.exclude(Patient_ID = patient.Patient_ID)

		return render_to_response('search_list.html', {'patients':patients, 'doctor': doctor_id })

	return render_to_response('search.html', {'doctor':doctor_id}, context_instance=RequestContext(request))
