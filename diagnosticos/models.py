from django.db import models
from solicitudes_servicio.models import SolicitudServicio
from tecnicos.models import Tecnico

class Diagnostico(models.Model):
    solicitud = models.ForeignKey(SolicitudServicio, on_delete=models.CASCADE, related_name='diagnosticos', verbose_name="Solicitud de Servicio")
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, related_name='diagnosticos', verbose_name="Técnico")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Diagnóstico")
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return f"Diagnóstico {self.id} - {self.solicitud.cliente.nombre} {self.solicitud.cliente.apellido}"
