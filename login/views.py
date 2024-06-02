from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.



class Vregistro(View):
    
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registro/registro.html',{'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST) #almaceno la informacion del formulario
        if form.is_valid():
            
            usuario = form.save() #guarda la info en la base de datos
            
            login(request, usuario) #logea al usuario con la informacion llenada
            
            return redirect('inicio')
        else:
            for msg in form.error_messages:                      
                messages.error(request,form.error_messages[msg])    #mostramos los errores que se almacenaron
                
            return render(request, 'registro/registro.html', {'form':form})        
            