from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from .views import *

app_name='transacciones'

urlpatterns = [

    url(regex=r"^registrar$", view=crear_transaccion, name="registrar_transaccion"),
    url(regex=r"^listado_ingresos$", view=mis_ingresos, name="listado_de_ingresos"),
    url(regex=r"^listado_egresos$", view=mis_egresos, name="listado_de_egresos"),
 
]
