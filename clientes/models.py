from django.db import models

class Cliente(models.Model):
    identificacion = models.CharField(max_length=20, unique=True, verbose_name="Identificación")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    correo = models.EmailField(verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    direccion = models.TextField(verbose_name="Dirección")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"