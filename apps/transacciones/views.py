from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from apps.presupuestos.models import Presupuesto, Categoria
from apps.cuentas.models import Cuenta

from .forms import TransaccionForm
from .models import Transaccion
from .models import Cuenta


@login_required
def crear_transaccion(request):

	form = TransaccionForm(usuario=request.user)
	if request.method == "POST":
		form = TransaccionForm(request.POST, usuario=request.user)
		if form.is_valid():
			transaccion = form.save()
			transaccion.save()
			if transaccion.tipo == 'Egreso':
				transaccion.cuenta.saldo -= transaccion.valor
				transaccion.categoria.actual += transaccion.valor
				transaccion.categoria.presupuesto.total_actual +=transaccion.valor
				transaccion.categoria.diferencia -= transaccion.valor
				transaccion.cuenta.save()
				transaccion.categoria.save()
				transaccion.categoria.presupuesto.save()
			else:
				transaccion.cuenta.saldo += transaccion.valor
				transaccion.cuenta.save()
			messages.success(request, 'La transacción se registró correctamente.')
			return redirect('presupuestos:listado_de_presupuestos')
		else:
			messages.error(request, "Error")
	return render(request, 'transacciones/transaccion_form.html', {'form':form})

@login_required
def mis_ingresos(request):
	cuentas = Cuenta.objects.filter(usuario=request.user.id)
	transacciones = []
	for i in range(len(cuentas)):
		transaccionesIn = Transaccion.objects.filter(tipo='Ingreso', cuenta=cuentas[i])
		if len(transaccionesIn) != 0:
			for i in range(len(transaccionesIn)):
				transacciones.append(transaccionesIn[i])
	return render(request, 'transacciones/listado_de_transacciones.html',{'transacciones':transacciones})

@login_required
def mis_egresos(request):
	cuentas = Cuenta.objects.filter(usuario=request.user.id)
	transacciones = []
	for i in range(len(cuentas)):
		transaccionesIn = Transaccion.objects.filter(tipo='Egreso', cuenta=cuentas[i])
		if len(transaccionesIn) != 0:
			for i in range(len(transaccionesIn)):
				transacciones.append(transaccionesIn[i])
	return render(request, 'transacciones/listado_de_transacciones.html',{'transacciones':transacciones})