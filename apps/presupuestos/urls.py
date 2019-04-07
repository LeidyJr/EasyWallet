from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from .views import *

app_name='presupuestos'

urlpatterns = [

    url(regex=r"^registrar$", view=crear_presupuesto, name="registrar_presupuesto"),
    url(regex=r"^listado$", view=mis_presupuestos, name="listado_de_presupuestos"),
    url(r'^editar/(?P<pk>\d+)/$', view=EditarPresupuesto.as_view(), name='editar_presupuesto'),
    url(r'^desactivar/(?P<id_presupuesto>\d+)/$', view=desactivar_presupuesto, name='desactivar_presupuesto'),
    url(regex=r"^registrar_categoria/(?P<id_presupuesto>[\w-]+)$", view=crear_categoria, name="registrar_categoria"),
    url(regex=r"^listado_de_categorias/(?P<id_presupuesto>[\w-]+)$", view=listado_de_categorias_del_presupuesto, name="listado_de_categorias"),
    url(regex=r"^editar_categoria/(?P<pk>[\w-]+)$", view=EditarCategoriaF, name="editar_categoria"),
]
