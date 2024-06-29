# Generated by Django 5.0.6 on 2024-06-26 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(max_length=20, unique=True, verbose_name='Identificación')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo Electrónico')),
                ('telefono', models.CharField(max_length=15, verbose_name='Teléfono')),
                ('direccion', models.TextField(verbose_name='Dirección')),
            ],
        ),
    ]
