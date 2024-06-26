from django.urls import path
from .views import crear_tecnico, listar_tecnicos, editar_tecnico, eliminar_tecnico

urlpatterns = [
    path('crear/', crear_tecnico, name='crear_tecnico'),
    path('', listar_tecnicos, name='listar_tecnicos'),
    path('editar/<int:id>/', editar_tecnico, name='editar_tecnico'),
    path('eliminar/<int:id>/', eliminar_tecnico, name='eliminar_tecnico'),
]
