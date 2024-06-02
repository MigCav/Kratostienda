from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.



class Vregistro(View):
    
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registro/registro.html')
    
    def post(self, request):
        pass