from django import forms
from django.core.exceptions import ValidationError
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
import datetime

from .models import Cuenta

class CuentaForm(forms.ModelForm):

	class Meta:
		model = Cuenta
		fields = ("nombre" , "saldo", "tipo", "estado", )
		labels = {
		"nombre": "Nombre: ",
		"saldo": "Saldo: ", 
		"tipo": "Tipo: ",
		"estado": "Estado: "
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
	def clean_estado(self):
		data = self.cleaned_data.get('estado')
		return data
class EditarCuentaForm(forms.ModelForm):
	class Meta:
		model = Cuenta
		fields = ("nombre" ,"tipo", "estado", )
		labels = {
		"nombre": "Nombre: ", 
		"tipo": "Tipo: ",
		"estado": "Estado: "
		}