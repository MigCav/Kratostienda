from django.urls import path

from . import views

app_name = 'carro'

urlpatterns = [
    
    path("agregar/<int:producto_id>/", views.agregar_productos, name='agregar'),
    path("restar/<int:producto_id>/", views.restar_productos, name='restar'),
    path("limpiar/", views.limpiar_carrito, name='limpiar'),
    path("eliminar/<int:producto_id>/", views.eliminar_productos, name='eliminar'),
    
]

