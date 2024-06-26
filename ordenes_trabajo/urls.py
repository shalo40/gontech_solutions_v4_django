from django.urls import path
from .views import crear_orden_trabajo, listar_ordenes_trabajo, editar_orden_trabajo, eliminar_orden_trabajo

urlpatterns = [
    path('crear/', crear_orden_trabajo, name='crear_orden_trabajo'),
    path('', listar_ordenes_trabajo, name='listar_ordenes_trabajo'),
    path('editar/<int:id>/', editar_orden_trabajo, name='editar_orden_trabajo'),
    path('eliminar/<int:id>/', eliminar_orden_trabajo, name='eliminar_orden_trabajo'),
]
