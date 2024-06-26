from django.urls import path
from .views import crear_presupuesto, listar_presupuestos, editar_presupuesto, eliminar_presupuesto

urlpatterns = [
    path('crear/', crear_presupuesto, name='crear_presupuesto'),
    path('', listar_presupuestos, name='listar_presupuestos'),
    path('editar/<int:id>/', editar_presupuesto, name='editar_presupuesto'),
    path('eliminar/<int:id>/', eliminar_presupuesto, name='eliminar_presupuesto'),
]
