# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from Apps.Mostrar.models import  Persona
from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'templates/index.html')

def ListaUAntofagasta(request):
    datos = Persona.objects.all()
    contexto = {'persona':datos}
    return render(request, 'templates/ListaUAntofagasta.html', contexto)


def ListaUSACH(request):
    datos = Persona.objects.all()
    contexto = {'persona':datos}
    return render(request, 'templates/ListaUSACH.html', contexto)

def ListaUTEM(request):
    datos = Persona.objects.all()
    contexto = {'persona':datos}
    return render(request, 'templates/ListaUtem.html', contexto)

