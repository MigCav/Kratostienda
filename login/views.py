from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.



class Vregistro(View):
    
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registro/registro.html', {'form':form})
    
    def post(self, request):
        
        form=UserCreationForm(request.POST) #almaceno la informacion en la variable form
        
        if form.is_valid(): #verifico si la informacion es valida y actuo de la sig manera
            
            usuario = form.save() #guarda la informacion en la BBDD
            
            login(request, usuario) #logea directamente al usuario en su cuenta
            
            return redirect('Home') 
        else:
             
            for msg in form.error_messages:                      #recorremos los errores ingresados
                messages.error(request,form.error_messages[msg])    #mostramos los errores que se almacenaron
                
            return render(request, 'registro/registro.html', {'form':form})        
            
            
def cerrar_sesion(request):
    
    logout(request)
    
    return redirect('Home')

def logear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST) #guardamos la informacion recibida en la variable
        if form.is_valid(): 
            nombre_usuario = form.cleaned_data.get('username') #cleaned_data.get() para obtener la informacion del recuadro X
            contraseña = form.cleaned_data.get('password')
            usuario = authenticate(username = nombre_usuario, password = contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')       
        else:
            messages.error(request, "Informacion incorrecta")
                  
    form = AuthenticationForm()
    return render(request, 'logear/logear.html', {'form':form})