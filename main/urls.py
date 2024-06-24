# main/urls.py

from django.urls import path
from .views import index, crear_cliente

urlpatterns = [
    path('', index, name='index'),
    path('crear_cliente/', crear_cliente, name='crear_cliente'),
    # Añadir más rutas para los otros modelos
]
