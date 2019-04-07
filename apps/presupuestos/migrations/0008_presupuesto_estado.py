# Generated by Django 2.1.7 on 2019-04-07 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0007_presupuesto_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=20),
        ),
    ]
