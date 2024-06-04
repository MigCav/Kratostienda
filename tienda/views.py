from django.shortcuts import render
from .models import producto, Categoria
# Create your views here.

productos = producto.objects.all()      # guarda todos los productos existentes en la variable
categoria = Categoria.objects.all()     # guarda todas las categorias existentes en la variable

def tienda(request):
    
    return render(request, 'tienda/tienda.html', {'producto': productos, 'categoria': categoria})


def categoriaf(request, categorias_id):                                  # recibe el id de la categoria buscada en otra pag
    categoria_tienda = Categoria.objects.get(id = categorias_id)         # obtiene la categoria asociada al id
    productosf = producto.objects.filter(categorias = categoria_tienda)     # rescata los productos asociados a esa categoria
    categorias = Categoria.objects.all()
    
    return render(request, 'tienda/categorias.html', {'categoria_tienda' : categoria_tienda, 'productos_filtrados' : productosf, 'categorias' : categorias})
