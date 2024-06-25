from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('clientes/', include('clientes.urls')),
    path('historiales_clientes/', include('historiales_clientes.urls')),
    path('solicitudes_servicio/', include('solicitudes_servicio.urls')),
    path('tecnicos/', include('tecnicos.urls')),
    path('ordenes_trabajo/', include('ordenes_trabajo.urls')),
    path('equipos/', include('equipos.urls')),
    path('presupuestos/', include('presupuestos.urls')),
    path('diagnosticos/', include('diagnosticos.urls')),
    path('pagos/', include('pagos.urls')),
    path('pruebas_diagnostico/', include('pruebas_diagnostico.urls')),
    path('solicitudes_repuestos/', include('solicitudes_repuestos.urls')),
    path('ordenes_compra/', include('ordenes_compra.urls')),
    path('historiales_ordenes_trabajo/', include('historiales_ordenes_trabajo.urls')),
    path('servicios_realizados/', include('servicios_realizados.urls')),
    path('registros_fotograficos/', include('registros_fotograficos.urls')),
]
