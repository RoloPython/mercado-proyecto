from django.urls import path
from . import views

urlpatterns = [
    # Rutas de Productos (Comentadas temporalmente)
    # path('productos/', views.lista_productos, name='lista_productos'),
    # path('productos/nuevo/', views.agregar_producto, name='agregar_producto'),

    # Clientes
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/nuevo/', views.agregar_cliente, name='agregar_cliente'),

    # Ventas
    path('ventas/', views.lista_ventas, name='lista_ventas'),
    path('ventas/nueva/', views.agregar_venta, name='agregar_venta'),
]