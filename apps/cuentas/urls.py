from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from .views import *

app_name='cuentas'

urlpatterns = [

    url(regex=r"^registrar$", view=crear_cuenta, name="registrar_cuenta"),
    url(regex=r"^listado$", view=mis_cuentas, name="listado_de_cuentas"),
    url(r'^editar/(?P<pk>\d+)/$', view=EditarCuenta.as_view(), name='editar_cuenta'),
    url(r'^ver/(?P<pk>\d+)/$', view=ver_cuenta, name='ver_cuenta'),
    url(r'^getGraficArea/(?P<pk>\d+)/$', view=getGraficArea, name="getGraficArea"),
]
