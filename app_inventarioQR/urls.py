from django.urls import path
from . import views


urlpatterns = [
    path('',views.inventario_main,name="inventario_main"),    
]
