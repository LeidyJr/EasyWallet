from django.db import models

from apps.usuarios.models import User

class Cuenta(models.Model):

    TIPO=(
		('Credito', 'Credito'),
		('Debito', 'Debito')
		)

    ESTADO=(
		('Activa', 'Activa'),
		('Inactiva', 'Inactiva')
		)
    
    nombre = models.CharField(max_length=25, verbose_name="Nombre de la cuenta")
    saldo = models.IntegerField()
    tipo = models.CharField(max_length=20, choices=TIPO, default= 'Debito')
    estado = models.CharField(max_length=20, choices=ESTADO, default= 'Activa')
    usuario = models.ForeignKey(User, related_name="cuentas_del_usuario", on_delete=models.CASCADE) 

    def __str__(self):
        return ("%s   %s   (%s)"%(self.nombre, self.tipo, self.saldo))
