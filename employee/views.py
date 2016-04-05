from forms import EmplyoeeForm
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from practitioner.models import Practitioner
from django.http import HttpResponse
from employee.models import Employee
from django.contrib.auth.models import User
from doctor.models import Patient
from appointments.models import Appointment
from practitioner.models import Practitioner
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext


# Create your views here.

def update1(request):
	if request.POST:
		form = EmplyoeeForm(request.POST,request.FILES)
		print "hello1"
		if form.is_valid():
			form.save()
			print "hello"
			return HttpResponseRedirect('/employee/update')

	else:
		form = EmplyoeeForm()

	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('update.html', args)

def update(request):
    return render_to_response('update_done.html')
       