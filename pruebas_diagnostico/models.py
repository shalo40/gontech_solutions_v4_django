from django.db import models
from diagnosticos.models import Diagnostico

class PruebaDiagnostico(models.Model):
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, related_name='pruebas', verbose_name="Diagnóstico")
    prueba = models.CharField(max_length=100, verbose_name="Prueba")
    resultado = models.CharField(max_length=100, verbose_name="Resultado")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de la Prueba")

    def __str__(self):
        return f"Prueba {self.prueba} - Resultado: {self.resultado}"
