from django.db import models
from solicitudes_repuestos.models import SolicitudRepuesto

class OrdenCompra(models.Model):
    solicitud_repuesto = models.ForeignKey(SolicitudRepuesto, on_delete=models.CASCADE, related_name='ordenes_compra', verbose_name="Solicitud de Repuesto")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    proveedor = models.CharField(max_length=100, verbose_name="Proveedor")
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto")

    def __str__(self):
        return f"Orden de Compra {self.id} - {self.proveedor}"
