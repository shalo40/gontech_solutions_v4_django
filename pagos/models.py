from django.db import models
from clientes.models import Cliente

class Pago(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pagos', verbose_name="Cliente")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Pago")
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto")
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return f"Pago {self.id} - {self.monto} CL"
