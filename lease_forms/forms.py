from django import forms

from .models import LeaseModel


class LeaseModelForm (forms.ModelForm):	 
	date_today =	forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'required': 'required'}))
	class Meta:
		 model = LeaseModel
		 fields = [
		 	'date_today',
		 	'tenant',
		 	'rate',
		 	'address',
		 	'location',
		 	'area',
		 	'advance',
		 	'deposit',
		 	'start_date',
		 	'end_date',
		 	'escalation'
		 ]
	def __init__(self, *args, **kwargs):
		super(LeaseModelForm, self).__init__(*args, **kwargs)
		self.fields['advance'].disabled = True