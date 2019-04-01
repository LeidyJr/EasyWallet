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


@login_required
def crear_transaccion(request):

    form_class = TransaccionForm
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            transaccion = form.save(commit=False)
            transaccion.descripcion = form.cleaned_data["descripcion"]
            transaccion.valor = form.cleaned_data["valor"]
            transaccion.tipo = form.cleaned_data["tipo"]
            transaccion.cuenta = form.cleaned_data["cuenta"]
            transaccion.categoria = form.cleaned_data["categoria"]
            transaccion.save()
            if transaccion.tipo == 'Egreso':

            	transaccion.cuenta.saldo -= transaccion.valor
            	transaccion.categoria.actual += transaccion.valor
            	transaccion.categoria.presupuesto.total_actual +=transaccion.valor
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
    return render(request, 'transacciones/transaccion_form.html', {'form':form_class()})

@login_required
def mis_ingresos(request):
    ingresos = request.cuenta.transacciones_de_la_cuenta.filter(estado='Ingreso')
    return render(request, 'transacciones/listado_de_transacciones.html',{'transacciones':ingresos})