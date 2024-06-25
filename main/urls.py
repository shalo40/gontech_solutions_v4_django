# main/urls.py

from django.urls import path
from .views import (
    index, crear_cliente, crear_historial_cliente, crear_solicitud_servicio, crear_tecnico, 
    crear_orden_trabajo, crear_equipo, crear_presupuesto, crear_diagnostico, crear_pago, 
    crear_prueba_diagnostico, crear_solicitud_repuesto, crear_orden_compra, 
    crear_historial_orden_trabajo, crear_servicio_realizado, crear_registro_fotografico
)

urlpatterns = [
    path('', index, name='index'),
    path('crear_cliente/', crear_cliente, name='crear_cliente'),
    path('crear_historial_cliente/', crear_historial_cliente, name='crear_historial_cliente'),
    path('crear_solicitud_servicio/', crear_solicitud_servicio, name='crear_solicitud_servicio'),
    path('crear_tecnico/', crear_tecnico, name='crear_tecnico'),
    path('crear_orden_trabajo/', crear_orden_trabajo, name='crear_orden_trabajo'),
    path('crear_equipo/', crear_equipo, name='crear_equipo'),
    path('crear_presupuesto/', crear_presupuesto, name='crear_presupuesto'),
    path('crear_diagnostico/', crear_diagnostico, name='crear_diagnostico'),
    path('crear_pago/', crear_pago, name='crear_pago'),
    path('crear_prueba_diagnostico/', crear_prueba_diagnostico, name='crear_prueba_diagnostico'),
    path('crear_solicitud_repuesto/', crear_solicitud_repuesto, name='crear_solicitud_repuesto'),
    path('crear_orden_compra/', crear_orden_compra, name='crear_orden_compra'),
    path('crear_historial_orden_trabajo/', crear_historial_orden_trabajo, name='crear_historial_orden_trabajo'),
    path('crear_servicio_realizado/', crear_servicio_realizado, name='crear_servicio_realizado'),
    path('crear_registro_fotografico/', crear_registro_fotografico, name='crear_registro_fotografico'),
]
