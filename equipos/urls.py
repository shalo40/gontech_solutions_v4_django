from django.urls import path
from .views import crear_equipo, listar_equipos, editar_equipo, eliminar_equipo

urlpatterns = [
    path('crear/', crear_equipo, name='crear_equipo'),
    path('', listar_equipos, name='listar_equipos'),
    path('editar/<int:id>/', editar_equipo, name='editar_equipo'),
    path('eliminar/<int:id>/', eliminar_equipo, name='eliminar_equipo'),
]
