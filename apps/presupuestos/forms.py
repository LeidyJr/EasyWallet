from django import forms

from .models import Presupuesto, Categoria

class PresupuestoForm(forms.ModelForm):
	class Meta:
		model = Presupuesto
		fields = ("nombre", "tipo",)
		labels = {
		"nombre": "Nombre: ", 
		"tipo":"Tipo:",
		}

	def clean_nombre(self):
		data = self.cleaned_data.get('nombre')
		return data


	def clean_tipo(self):
		data = self.cleaned_data.get('tipo')
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