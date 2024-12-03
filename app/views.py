from django.shortcuts import render, HttpResponse
from app.models import Ciclista, Equipo, Prueba, Clasificacion
import json



def altaCiclista(request):
    return render(request, 'altaCiclista.html')

def altaPrueba(request):
    if request.method == 'GET':
        ciclistas = Ciclista.objects.all()
        return render(request, 'altaPrueba.html', context={'ciclistas': ciclistas})
    
    if request.method == 'POST':
        print(request.POST)
        nueva_prueba = Prueba()
        nueva_prueba.nombre = request.POST['nombre']
        nueva_prueba.añoEdicion = request.POST['anioEdicion']
        nueva_prueba.cantidadEtapas = request.POST['cantidadEtapas']
        nueva_prueba.kmsTotales = request.POST['kmsTotales']
        nueva_prueba.ganador = Ciclista.objects.get(pk=request.POST['ganadorId'])
        nueva_prueba.save()
        clasificacion = request.POST['clasificacion-input']
        clasificacion = json.loads(clasificacion)
        # clasificacion = [ {posicion:int, equipo:int}, ... ]
        
        clasificaciones = [
            Clasificacion(
            prueba=nueva_prueba,
            posicion=item['posicion'],
            equipo=Equipo.objects.get(pk=item['equipo'])
            ) for item in clasificacion
        ]
        
        Clasificacion.objects.bulk_create(clasificaciones)
        print(nueva_prueba.id)

        return HttpResponse('Prueba guardada correctamente')

def altaClasificacion(request):
    if request.method == 'GET':
        equipos = Equipo.objects.all()
        return render(request, 'altaClasificacion.html', context={'equipos': equipos})
    
def main(request):
    if request.method == 'GET':
        ciclistas = Ciclista.objects.all()
        equipos = Equipo.objects.all()
        return render(request, 'index.html', context={'ciclistas': ciclistas, 'equipos': equipos})