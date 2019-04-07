from django.db import models
from django.utils import timezone

from apps.usuarios.models import User

class Presupuesto(models.Model):
	TIPOS=(
		('Egreso','Egreso'),
		('Ingreso','Ingreso'),
		)
	ESTADOS=(
		('Activo','Activo'),
		('Inactivo','Inactivo'),
		)

	nombre = models.CharField(max_length=15, verbose_name="Nombre del presupuesto")#universidad
	mes = models.DateField(editable=False)#agosto
	total_planeado = models.IntegerField()
	total_actual =models.IntegerField()
	tipo = models.CharField(max_length=20,choices=TIPOS, default="Egreso")
	estado = models.CharField(max_length=20,choices=ESTADOS, default="Activo")
	usuario = models.ForeignKey(User, related_name="presupuestos_del_usuario", on_delete=models.CASCADE)

	def __str__(self):

		return ("%s %s (%s)"%(self.nombre, self.total_planeado, self.total_actual))

	def save(self, *args, **kwargs):

		if not self.id:
			self.mes = timezone.now()
		return super(Presupuesto, self).save(*args, **kwargs)

class Categoria(models.Model):

	nombre = models.CharField(max_length=15, verbose_name="Nombre de la categoría") #almuerzos
	planeado = models.IntegerField()#20000
	actual = models.IntegerField()
	diferencia = models.IntegerField()
	presupuesto = models.ForeignKey(Presupuesto, related_name="categorias_del_presupuesto", on_delete=models.CASCADE)

	def __str__(self):
		return ("%s "%(self.nombre))

