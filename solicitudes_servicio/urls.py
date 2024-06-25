from django.urls import path
from .views import crear_solicitud_servicio, listar_solicitudes_servicio, editar_solicitud_servicio, eliminar_solicitud_servicio

urlpatterns = [
    path('crear/', crear_solicitud_servicio, name='crear_solicitud_servicio'),
    path('', listar_solicitudes_servicio, name='listar_solicitudes_servicio'),
    path('editar/<int:id>/', editar_solicitud_servicio, name='editar_solicitud_servicio'),
    path('eliminar/<int:id>/', eliminar_solicitud_servicio, name='eliminar_solicitud_servicio'),
]
