from django.urls import path
from . import views

urlpatterns = [
    path('altaCiclista', views.altaCiclista),
    path('altaPrueba', views.altaPrueba),
    path('altaClasificacion', views.altaClasificacion),
    path('', views.main)
]
