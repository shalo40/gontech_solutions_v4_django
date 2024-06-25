from django.urls import path
from .views import crear_cliente, listar_clientes, editar_cliente, eliminar_cliente

urlpatterns = [
    path('crear/', crear_cliente, name='crear_cliente'),
    path('', listar_clientes, name='listar_clientes'),
    path('editar/<int:id>/', editar_cliente, name='editar_cliente'),
    path('eliminar/<int:id>/', eliminar_cliente, name='eliminar_cliente'),
]
