# Generated by Django 2.1.7 on 2019-03-31 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0005_auto_20190330_1957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presupuesto',
            old_name='total_real',
            new_name='total_actual',
        ),
        migrations.RenameField(
            model_name='presupuesto',
            old_name='total_presupuestado',
            new_name='total_planeado',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='actual',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='diferencia',
            field=models.IntegerField(),
        ),
    ]