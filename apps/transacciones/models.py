from django.db import models

from apps.cuentas.models import Cuenta
from apps.presupuestos.models import Categoria

class Transaccion(models.Model):
	TIPO=(
		('Ingreso', 'Ingreso'),
		('Egreso', 'Egreso')
		)

	fecha = models.DateField()
	descripcion = models.CharField(max_length=40, verbose_name="Descripción de la transacción")
	valor = models.IntegerField()
	cuenta = models.ForeignKey(Cuenta, related_name="transacciones_de_la_cuenta", on_delete= models.CASCADE)
	categoria = models.ForeignKey(Categoria, related_name="transacciones_de_la_categoria", on_delete=models.CASCADE)
	tipo = models.CharField(max_length=20, choices=TIPO, default= 'Egreso')