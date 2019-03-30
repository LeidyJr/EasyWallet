from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Cuenta
from .forms import CuentaForm

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
            return redirect('cuentas:listado_de_cuentas')
    else:
        form = CuentaForm()
    return render(request, 'cuentas/cuentas_form.html', {
        'form': form
    })

class ListarCuentas(ListView):
    model = Cuenta
    template_name = 'cuentas/listado_de_cuentas.html'
    queryset = Cuenta.objects.all()


class EditarCuenta(UpdateView):
    model = Cuenta
    form_class = CuentaForm
    template_name = 'cuentas/cuentas_form.html'
    success_message = "La cuenta %(name)s se modificó correctamente."
    success_url = reverse_lazy('cuentas:listado_de_cuentas')

