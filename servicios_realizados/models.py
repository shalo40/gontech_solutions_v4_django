from django.db import models
from ordenes_trabajo.models import OrdenTrabajo

class ServicioRealizado(models.Model):
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name='servicios_realizados', verbose_name="Orden de Trabajo")
    fecha_realizacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Realización")
    descripcion = models.TextField(verbose_name="Descripción del Servicio")

    def __str__(self):
        return f"Servicio Realizado {self.id} - {self.orden_trabajo.id}"
