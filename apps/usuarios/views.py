from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from functools import wraps
from chartjs.views.lines import BaseLineChartView

from apps.usuarios.forms import SignUpForm
from apps.usuarios.models import User
from apps.cuentas.models import Cuenta

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user.es_cliente =True
            user.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('cuentas:listado_de_cuentas')
    else:
        form = SignUpForm()
    return render(request, 'usuarios/signup.html', {'form': form})

def Inicio(request):
    cuentas = request.user.cuentas_del_usuario.filter(estado='Activa')
    presupuestos = request.user.presupuestos_del_usuario.filter(mes__month=4)
    print(presupuestos)
    return render(request,'usuarios/inicio.html',{'cuentas':cuentas})

class CuentasSaldo(BaseLineChartView):
    def get_labels(self):
        nombres_cuentas = list(Cuenta.objects.all().values_list("nombre", flat=True))
        return nombres_cuentas

    def get_providers(self):
        return [" Saldo "]

    def get_data(self):
        cuentas = Cuenta.objects.all()
        saldo_cuentas = []
        for cuenta in cuentas:
            saldo_cuenta = cuenta.saldo
            saldo_cuentas.append(saldo_cuenta)
        return [saldo_cuentas]

vista_cuentas_y_saldo = TemplateView.as_view(template_name='usuarios/inicio.html')
cuentas_y_saldo_json = CuentasSaldo.as_view()
