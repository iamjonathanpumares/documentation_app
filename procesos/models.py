# -*- coding: utf-8 -*-
from django.db import models
from proyectos.models import Proyecto
from documentacion.models import Modulo

TIPO_ACTIVIDAD_CHOICES = (
	('E', 'Entrada'),
	('P', 'Proceso'),
	('D', 'Decisión'),
	('S', 'Salida'),
)

class Proceso(models.Model):
	proyecto = models.ForeignKey(Proyecto, related_name='procesos', on_delete=models.CASCADE)
	nombre_proceso = models.CharField('Nombre del proceso', max_length=50)
	descripcion_proceso = models.TextField('Descripción del proceso')

	def __unicode__(self):
		return self.nombre_proceso

class Responsable(models.Model):
	proceso = models.ForeignKey(Proceso, related_name='responsables', on_delete=models.CASCADE)
	responsable = models.CharField('Responsable involucrado en el proceso', max_length=50)

	def __unicode__(self):
		return self.responsable

class Actividad(models.Model):
	proceso = models.ForeignKey(Proceso, related_name='actividades', on_delete=models.CASCADE)
	responsable = models.ForeignKey(Responsable, related_name='actividades', on_delete=models.CASCADE)
	nombre_actividad = models.CharField('Nombre de la actividad', max_length=150)
	tipo_actividad = models.CharField('Tipo de actividad', max_length=1, choices=TIPO_ACTIVIDAD_CHOICES)
	orden = models.PositiveSmallIntegerField()

	def __unicode__(self):
		return self.nombre_actividad