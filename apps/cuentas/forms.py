from django import forms
from django.core.exceptions import ValidationError
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
import datetime

from .models import Cuenta

class CuentaForm(forms.ModelForm):

	class Meta:
		model = Cuenta
		fields = ("nombre" , "saldo", "tipo", )
		labels = {
		"nombre": "Nombre: ",
		"saldo": "Saldo: ", 
		"tipo": "Tipo: "
		}

	def clean_nombre(self):
		data = self.cleaned_data.get('nombre')
		return data
	def clean_saldo(self):
		data = self.cleaned_data.get('saldo')
		return data
	def clean_tipo(self):
		data = self.cleaned_data.get('tipo')
		return data
