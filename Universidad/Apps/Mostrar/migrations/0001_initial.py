# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-09-30 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellidoP', models.CharField(max_length=20)),
                ('apellidoM', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=10)),
                ('remuneraciones', models.IntegerField()),
                ('estamento', models.CharField(max_length=20)),
                ('funcion', models.CharField(max_length=15)),
                ('universidad', models.CharField(max_length=10)),
                ('fecha_Ingreso', models.DateField()),
            ],
        ),
    ]
