from django.db import models
from django.utils import timezone

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
	categoria = models.ForeignKey(Categoria, related_name="transacciones_de_la_categoria", on_delete=models.CASCADE, null=True, blank=True)
	tipo = models.CharField(max_length=20, choices=TIPO, default= 'Egreso')
	saldo_actual_cuenta = models.IntegerField(default=100)

	def save(self, *args, **kwargs):

		if not self.id:
			self.fecha = timezone.now()
		return super(Transaccion, self).save(*args, **kwargs)
