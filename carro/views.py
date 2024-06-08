from django.shortcuts import render
from .carro import Carro
from tienda.models import producto
from django.shortcuts import redirect


# Create your views here.

def agregar_productos(request, producto_id):
    
    carro           =   Carro(request)
    producto_carro  =   producto.objects.get(id = producto_id)
    carro.agregar(producto = producto_carro)
    
    return redirect('tienda')

def restar_productos(request, producto_id):
    
    carro           =   Carro(request)
    producto_carro  =   producto.objects.get(id = producto_id)
    carro.restar_producto(producto = producto_carro)
    
    return redirect('tienda')

def limpiar_carrito(request):
    
    carro = Carro(request)
    carro.limpiar_carro()
    
    return redirect('tienda')

def eliminar_productos(request, producto_id):
    
    carro           =   Carro(request)
    producto_carro  =   producto.objects.get(id = producto_id)
    carro.eliminar_producto(producto = producto_carro)
    
    return redirect('tienda')
    
    