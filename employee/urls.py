from django.conf.urls import patterns, include, url

urlpatterns = patterns(
	'',
	url(r'^update_form/$', 'employee.views.update1'),
	url(r'^update/$', 'employee.views.update'),
	
	)