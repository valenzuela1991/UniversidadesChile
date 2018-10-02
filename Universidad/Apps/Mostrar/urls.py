from django.conf.urls import url , include
from django.contrib import admin
from Apps.Mostrar.views import ListaUAntofagasta , inicio
#from Apps.Mostrar.views import *


urlpatterns = [
    url(r'^lista', ListaUAntofagasta),
    url(r'^inicio', inicio),
]