# Generated by Django 2.1.7 on 2019-03-31 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0004_auto_20190330_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuesto',
            name='total_real',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]