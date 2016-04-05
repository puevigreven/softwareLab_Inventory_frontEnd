from django.conf.urls import patterns, include, url

urlpatterns = patterns(
	'',
	url(r'^get/(?P<appointment_id>\d+)/$', 'appointments.views.appointment'),
  #      url(r'^get/(?P<practitioner_id>\d+)/$', 'appointments.views.practitioner'),
	url(r'^all/$', 'appointments.views.appointments'),
	url(r'^create/$', 'appointments.views.create'),
	)
