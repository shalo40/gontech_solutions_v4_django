from django.db import models
from clientes.models import Cliente

class HistorialCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='historiales', verbose_name="Cliente")
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha")
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return f"Historial de {self.cliente.nombre} {self.cliente.apellido} el {self.fecha}"
