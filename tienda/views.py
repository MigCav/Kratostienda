from django.shortcuts import render

# Create your views here.



def prueba(request):
    return render(request, 'tienda/tienda.html')