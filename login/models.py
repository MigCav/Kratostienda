from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.


class formedit(UserCreationForm):
    telefono = forms.IntegerField(label='telefono', required=True)
    direccion = forms.CharField(label='direccion', max_length= 60, required=True)
    sexo = forms.ChoiceField(label='sexo', choices=[('Masculino'), ('Femenino')])
    
    class Meta:
        model   =   User
        fields  =   ('username', 'email', 'password1', 'password2', 'telefono', 'direccion', 'sexo')
        