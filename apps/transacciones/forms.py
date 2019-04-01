from django import forms

from .models import Transaccion

class TransaccionForm(forms.ModelForm):
	class Meta:
		model = Transaccion
		fields = ("descripcion", "valor", "cuenta", "categoria", "tipo", )
		labels = {
		"descripcion" : "Descripción: ",
		"valor" : "Valor: ",
		"cuenta" : "Cuenta: ",
		"categoria" : "Categoría: ",
		"tipo" : "Tipo: ", 
		}

	def clean_descripcion(self):
		data = self.cleaned_data.get('descripcion')
		return data
	def clean_valor(self):
		data = self.cleaned_data.get('valor')
		return data
	def clean_cuenta(self):
		data = self.cleaned_data.get('cuenta')
		return data
	def clean_categoria(self):
		data = self.cleaned_data.get('categoria')
		return data
	def clean_tipo(self):
		data = self.cleaned_data.get('tipo')
		return data
	