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
           
    
def cerrar_sesion(request):
    logout(request)
    return redirect('inicio') 

def logear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST) #guardamos la informacion recibida en la variable
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username') #para obtener la informacion acertada del recuadro usename
            contraseña = form.cleaned_data.get('password')
            usuario = authenticate(username = nombre_usuario, password = contraseña)
            
            if usuario is not None:         #si la informacion no es nula logea al usuario
                login(request, usuario)
                return redirect('inicio')
            
        
    form = AuthenticationForm()
    return render(request, 'logear/logear.html', {'form':form})