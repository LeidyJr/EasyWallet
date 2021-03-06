from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.core.serializers import serialize
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from apps.transacciones.models import Transaccion
from .models import Cuenta
from .forms import CuentaForm, EditarCuentaForm

@login_required
def crear_cuenta(request):
    if request.method == 'POST':
        form = CuentaForm(request.POST)
        if form.is_valid():
            cuenta = form.save(commit=False)
            cuenta.nombre = form.cleaned_data["nombre"]
            cuenta.saldo = form.cleaned_data["saldo"]
            cuenta.tipo = form.cleaned_data["tipo"]
            cuenta.usuario = request.user
            cuenta.save()
            transaccion = Transaccion(descripcion="Inicial",valor=cuenta.saldo, cuenta=cuenta, tipo="Inicial", saldo_actual_cuenta=cuenta.saldo)
            transaccion.save()
            messages.success(request, 'La cuenta se registró correctamente.')
            return redirect('cuentas:listado_de_cuentas')
        else:
            messages.error(request, 'No se pudo registrar la cuenta, por favor verifique los datos ingresados.')
    else:
        form = CuentaForm()
    return render(request, 'cuentas/cuentas_form.html', {
        'form': form
    })

@login_required
def mis_cuentas(request):
    cuentas = request.user.cuentas_del_usuario.filter(estado='Activa')
    return render(request, 'cuentas/listado_de_cuentas.html',{'cuentas':cuentas})


class EditarCuenta(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Cuenta
    form_class = EditarCuentaForm
    template_name = 'cuentas/cuentas_editar.html'
    success_message = "La cuenta %(nombre)s se modificó correctamente."
    success_url = reverse_lazy('cuentas:listado_de_cuentas')

@login_required
def ver_cuenta(request, pk):
    cuenta = Cuenta.objects.get(id=pk)
    return render(request,'cuentas/ver_cuenta.html', {'cuenta':cuenta})

def getGraficArea(request, pk):
    transacciones = Transaccion.objects.all().filter(cuenta=pk,fecha__month=4)#, fecha__month=4
    transacciones = [ {'fecha':transaccion.fecha, 'saldo':transaccion.saldo_actual_cuenta} for transaccion in transacciones]
    return HttpResponse(json.dumps(transacciones,cls=DjangoJSONEncoder), content_type = "application/json")