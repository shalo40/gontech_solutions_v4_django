from django.db import models
from ordenes_trabajo.models import OrdenTrabajo

class RegistroFotografico(models.Model):
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name='registros_fotograficos', verbose_name="Orden de Trabajo")
    imagen = models.ImageField(upload_to='fotos/', verbose_name="Imagen")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")

    def __str__(self):
        return f"Registro Fotográfico {self.id} - {self.orden_trabajo.id}"
