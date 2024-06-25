from django.db import models

class Tecnico(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    especialidad = models.CharField(max_length=100, verbose_name="Especialidad")
    correo = models.EmailField(verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"
