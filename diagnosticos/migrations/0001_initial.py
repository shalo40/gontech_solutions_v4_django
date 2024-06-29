# Generated by Django 5.0.6 on 2024-06-26 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('solicitudes_servicio', '0001_initial'),
        ('tecnicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Diagnóstico')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnosticos', to='solicitudes_servicio.solicitudservicio', verbose_name='Solicitud de Servicio')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnosticos', to='tecnicos.tecnico', verbose_name='Técnico')),
            ],
        ),
    ]
