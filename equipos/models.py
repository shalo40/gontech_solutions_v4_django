from django.db import models
from clientes.models import Cliente

class Equipo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Equipo")
    modelo = models.CharField(max_length=100, verbose_name="Modelo")
    numero_serie = models.CharField(max_length=100, unique=True, verbose_name="Número de Serie")
    fabricante = models.CharField(max_length=100, verbose_name="Fabricante")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='equipos', verbose_name="Cliente")
    fecha_adquisicion = models.DateField(verbose_name="Fecha de Adquisición")

    def __str__(self):
        return f"{self.nombre} - {self.modelo} ({self.numero_serie})"
