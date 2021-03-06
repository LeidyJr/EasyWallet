from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from functools import wraps
from chartjs.views.lines import BaseLineChartView
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.core.serializers import serialize

from apps.usuarios.forms import SignUpForm
from apps.usuarios.models import User
from apps.cuentas.models import Cuenta
from apps.presupuestos.models import *

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
    presupuestos = request.user.presupuestos_del_usuario.filter(estado="Activo")#mes__month=3
    contexto = {'cuentas':cuentas,'presupuestos':presupuestos}
    print("inicio")
    print(contexto) 
    return render(request,'usuarios/inicio.html', {'cuentas':cuentas,'presupuestos':presupuestos})

def presupuestos_serialize(presupuesto):
    categorias = presupuesto.categorias_del_presupuesto.all()
    categorias = [ {'categoria_nombre': categoria.nombre, 'categoria_planeado': categoria.planeado, 'categoria_actual':categoria.actual} for categoria in categorias]
    return {'id':presupuesto.id,'nombre':presupuesto.nombre, 'total_planeado':presupuesto.total_planeado, 'total_actual':presupuesto.total_actual, 'categorias':categorias}

def getGraficPie(request):
    presupuestos = request.user.presupuestos_del_usuario.filter(estado="Activo")
    presupuestos = [ presupuestos_serialize(presupuesto) for presupuesto in presupuestos ]
    return HttpResponse(json.dumps(presupuestos,cls=DjangoJSONEncoder), content_type = "application/json")

def getCuentas(request):
    cuentas = request.user.cuentas_del_usuario.filter(estado='Activa')
    cuentas = [ {'cuenta_id':cuenta.id} for cuenta in cuentas ]
    return HttpResponse(json.dumps(cuentas,cls=DjangoJSONEncoder), content_type = "application/json")

class CuentasSaldo(BaseLineChartView):

    def get_labels(self):
        nombres_cuentas = list(Cuenta.objects.filter(usuario=1).values_list("nombre", flat=True))
        return nombres_cuentas

    def get_providers(self):
        return [" NOTHING "]

    def get_data(self):
        cuentas = Cuenta.objects.all()
        saldo_cuentas = []
        for cuenta in cuentas:
            saldo_cuenta = cuenta.saldo
            saldo_cuentas.append(saldo_cuenta)
        return [saldo_cuentas]

vista_cuentas_y_saldo = TemplateView.as_view(template_name='usuarios/inicio.html')
cuentas_y_saldo_json = CuentasSaldo.as_view()
