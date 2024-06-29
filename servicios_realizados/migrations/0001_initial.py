# Generated by Django 5.0.6 on 2024-06-26 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ordenes_trabajo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicioRealizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_realizacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Realización')),
                ('descripcion', models.TextField(verbose_name='Descripción del Servicio')),
                ('orden_trabajo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicios_realizados', to='ordenes_trabajo.ordentrabajo', verbose_name='Orden de Trabajo')),
            ],
        ),
    ]
