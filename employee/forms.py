from django import forms
from models import Schedule
from models import Employee


class EmployeeForm(forms.ModelForm):

	class Meta:
		model = Employee
		fields = ('Patient_ID','Description','Credential', 'Date_Of_Upload')



class ScheduleForm(forms.ModelForm):

	class Meta:
		model = Schedule
		fields = ('r00','r01','r02','r03','r04','r05','r06','r10','r11','r12','r13','r14','r15','r16','r20','r21','r22','r23','r24','r25','r26','r30','r31','r32','r33','r34','r35','r36','r40','r41','r42','r43','r44','r45','r46','r50','r51','r52','r53','r54','r55','r56')