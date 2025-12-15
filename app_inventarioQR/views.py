from django.shortcuts import render

# Create your views here.

def inventario_main(request):
    return render(request,'inventario_main.html')