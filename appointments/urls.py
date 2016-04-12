from django.conf.urls import patterns, include, url

urlpatterns = patterns(
	'',
	url(r'get/(?P<doctor_id>\d+)/$', 'appointments.views.appointment'),
	url(r'all/(?P<patient_id>\d+)/$', 'appointments.views.appointments'),
	url(r'create/(?P<patient_id>\d+)/$', 'appointments.views.create'),
	url(r'availability/$', 'appointments.views.calendar'),
	)
