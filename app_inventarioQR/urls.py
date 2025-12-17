from django.urls import path
from . import views


urlpatterns = [
    path('/',views.inventario_main,name='inventario_main'),
    path('editar/',views.editar_objeto,name='editar_objeto'),    
]
