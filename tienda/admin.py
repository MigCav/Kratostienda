from django.contrib import admin
from .models import Categoria, producto
# Register your models here.



class producto_admin(admin.ModelAdmin):
    readonly_fields =   ('created', 'updated')

    
class Categoria_admin(admin.ModelAdmin):
    readonly_fields =   ('created', 'updated')
    
admin.site.register(Categoria, Categoria_admin)
admin.site.register(producto, producto_admin)