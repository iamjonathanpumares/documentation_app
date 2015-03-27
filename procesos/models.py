# -*- coding: utf-8 -*-
from django.db import models

class Proceso(models.Model):
	nombre_proceso = models.CharField('Nombre del proceso', max_length=50)
	descripcion_proceso = models.CharField('Descripción del proceso', max_length=50)

class Actividad(models.Model):
	nombre_actividad = models.CharField('Nombre de la actividad', max_length=50)
	proceso = models.ForeignKey(Proceso, related_name='actividades')
