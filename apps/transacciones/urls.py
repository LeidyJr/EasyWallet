from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from .views import *

app_name='transacciones'

urlpatterns = [

    url(regex=r"^registrar$", view=crear_transaccion, name="registrar_transaccion"),

]
