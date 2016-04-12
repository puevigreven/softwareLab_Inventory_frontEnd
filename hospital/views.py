from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from practitioner.models import Practitioner
from doctor.models import Patient
from pharmacist.models import Pharma
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from forms import MyRegistrationForm


def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	group = request.POST.get('group1','Patient')
	print group
	if group=='Patient':
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			patientID = user.id
			return HttpResponseRedirect('/accounts/loggedin/%s/' % patientID)
		
	if group=='Doctor':
		if Practitioner.objects.get(User_ID = username) == Practitioner.objects.get(Password = password) and Practitioner.objects.get(User_ID = username):
			args = {}
			arg_temp = {}
			arg_temp['get_id'] = Practitioner.objects.get(User_ID = username)
			args['patients'] = Patient.objects.filter( Doctor_Visited_Id = arg_temp['get_id'].id )
			link = arg_temp['get_id'].id
			return HttpResponseRedirect('/doctor/%s/all/' % link)

	if group=='Pharmacist':
		if Pharma.objects.get(User_ID = username) == Pharma.objects.get(Password = password) and Pharma.objects.get(User_ID = username):
			return HttpResponseRedirect('/inventory')
		
	else:
		return HttpResponseRedirect('/accounts/invalid')


def loggedin(request, patient_id = 1):
	user = User.objects.get(id = patient_id)
	args = {}
	args['full_name'] = user.first_name
 	args['username'] = user.username
	args['userid'] = user.id
	args['date_joined'] = user.date_joined.date    
	return render_to_response('loggedin.html', args)

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')


def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		handle = open('/home/rishabh/hospital/counter.txt', 'r+')
		count = int(handle.read())
		handle.close()
		if form.is_valid():
			temp = request.POST.get('username','')
			form.setID('s'+str(count+1))
			trans = 's'+str(count+1)
			form.setName(temp)
			handle1 = open('/home/rishabh/hospital/counter.txt', 'w')
			handle1.write(str(count+1))
			handle1.close()
			form.save()
			registerID = User.objects.get( username = 's'+str(count+1))
			return HttpResponseRedirect('/accounts/register_success/%s/' % registerID.id)
	args={}
	args.update(csrf(request))
	args['form']=MyRegistrationForm()
	return render_to_response('register.html', args)


def register_success(request, patient_id =1):
	user = User.objects.get(id = patient_id)
	return render_to_response('register_success.html', {'username':user.username})
