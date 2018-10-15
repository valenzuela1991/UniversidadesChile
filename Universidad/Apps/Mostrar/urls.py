from django.conf.urls import url , include
from django.contrib import admin
from Apps.Mostrar.views import inicio, ListaUAntofagasta , ListaUSACH, ListaUTEM


urlpatterns = [
    url(r'^$', inicio),
    url(r'^listaAntofagasta', ListaUAntofagasta),
    url(r'^listaUSACH', ListaUSACH),
    url(r'^listaUTEM', ListaUTEM),
    ]