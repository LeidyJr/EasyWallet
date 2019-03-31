from django import forms

from .models import Presupuesto, Categoria

class PresupuestoForm(forms.ModelForm):
	class Meta:
		model = Presupuesto
		fields = ("nombre", )
		labels = {
		"nombre": "Nombre: ", 
		}

	def clean_nombre(self):
		data = self.cleaned_data.get('nombre')
		return data
	

class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria
		fields= ("nombre", "planeado", )
		labels = {
		"nombre" : "Nombre: ",
		"planeado" : "Planeado: "
		}

	def clean_nombre(self):
		data = self.cleaned_data.get('nombre')
		return data
	def clean_planeado(self):
		data = self.cleaned_data.get('planeado')
		return data