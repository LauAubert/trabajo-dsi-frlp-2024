from django.contrib import admin
from .models import *

class ClasificacionInline(admin.TabularInline):
    model = Clasificacion
    extra = 1

class PruebaAdmin(admin.ModelAdmin):
    inlines = [ClasificacionInline]

# Register your models here.
admin.site.register(Pais)
admin.site.register(Ciclista)
admin.site.register(Director)
admin.site.register(Equipo)
admin.site.register(Prueba, PruebaAdmin)
admin.site.register(Clasificacion)