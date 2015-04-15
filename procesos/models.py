# -*- coding: utf-8 -*-
from django.db import models
from proyectos.models import Proyecto
from documentacion.models import Modulo

class Proceso(models.Model):
	proyecto = models.ForeignKey(Proyecto, related_name='procesos')
	modulos = models.ManyToManyField(Modulo, related_name='modulos')
	nombre_proceso = models.CharField('Nombre del proceso', max_length=50)
	descripcion_proceso = models.TextField('Descripción del proceso')

	def __unicode__(self):
		return self.nombre_proceso

class Actividad(models.Model):
	proceso = models.ForeignKey(Proceso, related_name='actividades')
	modulo = models.ForeignKey(Modulo, related_name='actividades', null=True, blank=True)
	nombre_actividad = models.CharField('Nombre de la actividad', max_length=50)
	orden = models.PositiveSmallIntegerField()

	def __unicode__(self):
		return self.nombre_actividad

