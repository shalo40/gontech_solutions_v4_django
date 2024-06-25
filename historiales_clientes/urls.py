from django.urls import path
from .views import crear_historial_cliente, listar_historiales_clientes, editar_historial_cliente, eliminar_historial_cliente

urlpatterns = [
    path('crear/', crear_historial_cliente, name='crear_historial_cliente'),
    path('', listar_historiales_clientes, name='listar_historiales_clientes'),
    path('editar/<int:id>/', editar_historial_cliente, name='editar_historial_cliente'),
    path('eliminar/<int:id>/', eliminar_historial_cliente, name='eliminar_historial_cliente'),
]
