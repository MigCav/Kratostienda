from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Vregistro

urlpatterns = [
    
    path("", Vregistro.as_view(), name='registro'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)