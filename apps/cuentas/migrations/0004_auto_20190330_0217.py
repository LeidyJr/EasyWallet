# Generated by Django 2.1.7 on 2019-03-30 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0003_auto_20190330_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='nombre',
            field=models.CharField(max_length=25, verbose_name='Nombre de la cuenta'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cuentas_del_usuario', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]