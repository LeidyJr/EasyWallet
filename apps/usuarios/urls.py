from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from .views import *

app_name='usuarios'

urlpatterns = [
    url('signup', signup, name='signup'),
    url('inicio', view=Inicio, name='inicio'),
    path('cuentas_y_saldo', vista_cuentas_y_saldo, name="cuentas_y_saldo"),
    path('cuentas_y_saldo_json', cuentas_y_saldo_json, name="cuentas_y_saldo_json"),
    path('getGraficPie', view=getGraficPie, name="getGraficPie"),
    ]