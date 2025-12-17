from django.shortcuts import render

# Create your views here.

def inventario_main(request):
    return render(request,'inventario_main.html')

def editar_objeto(request):
    return render(request,'formulario_agregar_objeto.html')