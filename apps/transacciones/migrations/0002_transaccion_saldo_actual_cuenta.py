# Generated by Django 2.1.7 on 2019-04-08 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaccion',
            name='saldo_actual_cuenta',
            field=models.IntegerField(default=100),
        ),
    ]