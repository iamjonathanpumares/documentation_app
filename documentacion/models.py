# -*- coding: utf-8 -*-
from django.db import models
from proyectos.models import Proyecto

class Modulo(models.Model):
	modulos_depende = models.ManyToManyField('self', related_name='submodulos', symmetrical=False)
	proyecto = models.ForeignKey(Proyecto, related_name='modulos')
	nombre_modulo = models.CharField('Nombre del módulo', max_length=35)
	descripcion_modulo = models.TextField('Descripción del módulo')
	nivel = models.PositiveSmallIntegerField('Nivel del módulo')

	def __unicode__(self):
		return self.nombre_modulo

"""class Submodulos(models.Model):
	modulo = models.ForeignKey(Modulo, related_name='submodulos')
	submodulo = models.ForeignKey(Modulo, related_name='modulos')

	def __unicode__(self):
		return '%s - %s' % (self.modulo.nombre_modulo, self.submodulo.nombre_modulo)"""

class TipoPaquete(models.Model):
	clave_paquete = models.CharField('Clave del paquete', max_length=5, unique=True)
	tipo_paquete = models.CharField('Tipo del paquete', max_length=50)

	def __unicode__(self):
		return self.tipo_paquete

class Paquete(models.Model):
	paquetes_requeridos = models.ManyToManyField('self', related_name='paquetes_dependen')
	modulo = models.ForeignKey(Modulo, related_name='paquetes')
	tipo_paquete = models.ForeignKey(TipoPaquete, related_name='paquetes')
	nombre_paquete = models.CharField('Nombre del paquete', max_length=35)
	descripcion_paquete = models.TextField('Descripción del paquete (opcional)', blank=True)

	def __unicode__(self):
		return self.nombre_paquete
