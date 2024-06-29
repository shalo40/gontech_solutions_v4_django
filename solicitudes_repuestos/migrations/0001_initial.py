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
            name='SolicitudRepuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repuesto', models.CharField(max_length=100, verbose_name='Repuesto Solicitado')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Solicitud')),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Pendiente', max_length=50, verbose_name='Estado')),
                ('orden_trabajo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes_repuesto', to='ordenes_trabajo.ordentrabajo', verbose_name='Orden de Trabajo')),
            ],
        ),
    ]
