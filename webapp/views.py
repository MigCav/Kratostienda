from django.shortcuts import render
from carro.carro import Carro

# Create your views here.

def inicio(request):
    
    carro = Carro(request)
    
    return render(request, "webapp/inicio.html")