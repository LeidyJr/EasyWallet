from django.db import models

from apps.usuarios.models import User

class Presupuesto(models.Model):

	nombre = models.CharField(max_length=15, verbose_name="Nombre del presupuesto")#universidad
	mes = models.DateField()#agosto
	total_presupuestado = models.IntegerField()
	total_real =models.IntegerField()
	usuario = models.ForeignKey(User, related_name="presupuestos_del_usuario", on_delete=models.CASCADE)


class Categoria(models.Model):

	nombre = models.CharField(max_length=15, verbose_name="Nombre de la categoría") #almuerzos
	planeado = models.IntegerField()#20000
	actual = models.IntegerField(blank=True)
	diferencia = models.IntegerField(blank=True)
	presupuesto = models.ForeignKey(Presupuesto, related_name="categorias_del_presupuesto", on_delete=models.CASCADE)
