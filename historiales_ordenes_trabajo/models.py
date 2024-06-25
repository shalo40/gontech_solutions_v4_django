from django.db import models
from ordenes_trabajo.models import OrdenTrabajo

class HistorialOrdenTrabajo(models.Model):
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name='historiales', verbose_name="Orden de Trabajo")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return f"Historial de Orden {self.orden_trabajo.id} el {self.fecha}"
