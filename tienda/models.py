from django.db import models
from django.forms import BooleanField

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now= True)
    created = models.DateTimeField(auto_now_add= True)
    
    class meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
    
    def __str__(self):
        return self.nombre
    
class producto(models.Model):
    nombre = models.CharField(max_length= 24)
    precio = models.FloatField()
    codigo = models.IntegerField(default= 0)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    disponibilidad = models.BooleanField(default= True)
    imagen = models.ImageField(upload_to="Tienda")
    categorias = models.ManyToManyField(Categoria)
    
    class meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
    
    def __str__(self):
        return self.nombre
    
