from django.db import models
from tecnicos.models import Tecnico
from solicitudes_servicio.models import SolicitudServicio


class OrdenTrabajo(models.Model):
    solicitud = models.ForeignKey(SolicitudServicio, on_delete=models.CASCADE, related_name='ordenes', verbose_name="Solicitud de Servicio")
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, related_name='ordenes', verbose_name="Técnico Asignado")
    fecha_asignacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Asignación")
    estado = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Completada', 'Completada')], default='Pendiente', verbose_name="Estado")
    descripcion = models.TextField(verbose_name="Descripción de la Orden")

    def __str__(self):
        return f"Orden {self.id} - {self.estado}"
