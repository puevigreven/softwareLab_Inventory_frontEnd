from django.conf.urls import patterns, include, url

urlpatterns = patterns(
	'',
	(r'^$', 'inventory.views.home'),
	(r'^all_med/$', 'inventory.views.display_all_medicines'),
	(r'^get_med/(?P<batch_num>\w+)/$', 'inventory.views.display_medicine'),
	(r'^create/$', 'inventory.views.create'),
	(r'^search/$', 'inventory.views.searchMedicine'),
	(r'^outGoingPatients/$', 'inventory.views.outGoingPatients'),
	(r'^issueMedicines/(?P<batch_num>\w+)/$', 'inventory.views.issueMedicines'),
	(r'^refillMedicines/$', 'inventory.views.refillMedicines'),
	(r'^get_patients/(?P<patient_id>\w+)/$', 'inventory.views.get_patients'),
	(r'^issueMedicinestoPatient/(?P<patient_id>\w+)/$', 'inventory.views.issue_Medicines_Patient'),
	(r'^get_medicines/(?P<patient_id>\w+)/(?P<batch_num>\w+)/$', 'inventory.views.get_Medicines_Patient'),
	(r'^issueMedicines_toPatients/(?P<patient_id>\w+)/(?P<batch_num>\w+)/$', 'inventory.views.issueMedicines_toPatients'),

)