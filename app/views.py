from django.shortcuts import render


def altaCiclista(request):
    return render(request, 'altaCiclista.html')

def altaPrueba(request):
    return render(request, 'altaPrueba.html')

def altaClasificacion(request):
    return render(request, 'altaClasificacion.html') 