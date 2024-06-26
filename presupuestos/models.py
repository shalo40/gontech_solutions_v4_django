from django.db import models
from solicitudes_servicio.models import SolicitudServicio
from clientes.models import Cliente

class Presupuesto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    solicitud = models.ForeignKey(SolicitudServicio, on_delete=models.CASCADE, related_name='presupuestos', verbose_name="Solicitud de Servicio")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    total_estimado = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total Estimado")
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return f"Presupuesto {self.id} - {self.total_estimado} CL"
