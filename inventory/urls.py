from django.conf.urls import patterns, include, url

urlpatterns = patterns(
	'',
	(r'^$', 'inventory.views.home'),
	(r'^all_med/$', 'inventory.views.display_all_medicines'),
	(r'^get_med/(?P<med_name>\w+)/$', 'inventory.views.display_medicine'),
	(r'^create/$', 'inventory.views.create'),
	(r'^search/$', 'inventory.views.searchMedicine'),
	#(r'^outGoingPatients/$', 'inventory.views.outGoingPatients'),
	(r'^issueMedicines/(?P<med_name>\w+)/$', 'inventory.views.issueMedicines'),
	(r'^refillMedicines/$', 'inventory.views.refillMedicines'),

)

