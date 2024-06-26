# Generated by Django 5.0.6 on 2024-06-26 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historiales', to='clientes.cliente', verbose_name='Cliente')),
            ],
        ),
    ]
