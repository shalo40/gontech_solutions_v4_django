from django.contrib import admin
from .models import (
    Cliente, HistorialCliente, SolicitudServicio, Tecnico, OrdenTrabajo, Equipo, 
    Presupuesto, Diagnostico, Pago, PruebaDiagnostico, SolicitudRepuesto, 
    OrdenCompra, HistorialOrdenTrabajo, ServicioRealizado, RegistroFotografico
)

admin.site.register(Cliente)
admin.site.register(HistorialCliente)
admin.site.register(SolicitudServicio)
admin.site.register(Tecnico)
admin.site.register(OrdenTrabajo)
admin.site.register(Equipo)
admin.site.register(Presupuesto)
admin.site.register(Diagnostico)
admin.site.register(Pago)
admin.site.register(PruebaDiagnostico)
admin.site.register(SolicitudRepuesto)
admin.site.register(OrdenCompra)
admin.site.register(HistorialOrdenTrabajo)
admin.site.register(ServicioRealizado)
admin.site.register(RegistroFotografico)
