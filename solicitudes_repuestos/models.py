from django.db import models
from ordenes_trabajo.models import OrdenTrabajo

class SolicitudRepuesto(models.Model):
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name='solicitudes_repuesto', verbose_name="Orden de Trabajo")
    repuesto = models.CharField(max_length=100, verbose_name="Repuesto Solicitado")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    fecha_solicitud = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Solicitud")
    estado = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Pendiente', verbose_name="Estado")

    def __str__(self):
        return f"Solicitud de {self.repuesto} - {self.estado}"
