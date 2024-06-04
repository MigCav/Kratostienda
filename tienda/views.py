from django.shortcuts import render
from .models import producto, Categoria
# Create your views here.

productos = producto.objects.all()
categoria = Categoria.objects.all()

def tienda(request):
    
    return render(request, 'tienda/tienda.html', {'producto': productos, 'categoria': categoria})