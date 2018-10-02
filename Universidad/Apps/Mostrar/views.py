# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from Apps.Mostrar.models import  Persona


# Create your views here.
def ListaUAntofagasta(request):
    datos = Persona.objects.all()
    contexto = {'persona':datos}
    return render(request, 'templates/ListaUAntofagasta.html', contexto)


def inicio(request):
    return render(request, 'templates/index.html')
