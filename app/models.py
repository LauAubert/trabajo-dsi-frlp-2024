from django.db import models

# Create your models here.
class Pais(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion
    
class Ciclista(models.Model):
    apellido = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    nombre = models.CharField(max_length=50)
    nacionalidad = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Director(models.Model):
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    director = models.OneToOneField(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre     

class Prueba(models.Model):
    nombre = models.CharField(max_length=50)
    añoEdicion = models.IntegerField()
    cantidadEtapas = models.IntegerField()
    kmsTotales = models.IntegerField()
    ganador = models.ForeignKey(Ciclista, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Clasificacion(models.Model):
    posicion = models.IntegerField()
    prueba = models.ForeignKey(Prueba, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __str__(self):
        # return str(self.posicion) + ' ' + self.prueba.nombre + ' ' + self.equipo.nombre
        return f'{self.equipo.nombre} salió {self.posicion}° en la prueba "{self.prueba.nombre}"'

