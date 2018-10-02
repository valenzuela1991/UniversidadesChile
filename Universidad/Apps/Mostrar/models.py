from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellidoP = models.CharField(max_length=20)
    apellidoM = models.CharField(max_length=20)
    tipo = models.CharField(max_length=10)
    remuneraciones = models.IntegerField()
    estamento = models.CharField(max_length=20)
    funcion = models.CharField(max_length=15)
    universidad = models.CharField(max_length=10)
    fecha_Ingreso = models.CharField(max_length=10)
    fecha_Informacion = models.CharField(max_length=10)


    def __str__(self):
        return '{}'.format(self.nombre)