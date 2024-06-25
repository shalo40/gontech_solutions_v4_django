from django.db import models
from clientes.models import Cliente

class SolicitudServicio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='solicitudes', verbose_name="Cliente")
    fecha_solicitud = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Solicitud")
    tipo_servicio = models.CharField(max_length=100, verbose_name="Tipo de Servicio")
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return f"Solicitud de {self.tipo_servicio} por {self.cliente.nombre} {self.cliente.apellido} el {self.fecha_solicitud}"
