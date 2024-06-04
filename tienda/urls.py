from django.urls import path
from . import views



urlpatterns = [
    path("", views.tienda, name = 'tienda'),
    path("categorias/<int:categorias_id>", views.categoriaf, name = 'categoriaf'),
] 