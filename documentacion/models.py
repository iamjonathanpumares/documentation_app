# -*- coding: utf-8 -*-
from django.db import models
from proyectos.models import Proyecto

class Modulo(models.Model):
	modulo_depende = models.ForeignKey('self', related_name='submodulos', blank=True, null=True)
	modulo_principal = models.ForeignKey('self', related_name='submodulos_totales', blank=True, null=True)
	proyecto = models.ForeignKey(Proyecto, related_name='modulos')
	nombre_modulo = models.CharField('Nombre del módulo', max_length=35)
	descripcion_modulo = models.TextField('Descripción del módulo')
	nivel = models.PositiveSmallIntegerField('Nivel del módulo')
	path = models.CharField('Ruta del módulo', max_length=250)

	def __unicode__(self):
		return self.nombre_modulo

class TipoPaquete(models.Model):
	clave_paquete = models.CharField('Clave del paquete', max_length=5, unique=True)
	tipo_paquete = models.CharField('Tipo del paquete', max_length=50)

	def __unicode__(self):
		return self.tipo_paquete

class Paquete(models.Model):
	paquetes_requeridos = models.ManyToManyField('self', related_name='paquetes_dependen', symmetrical=False)
	proyecto = models.ForeignKey(Proyecto, related_name='paquetes')
	modulo = models.ForeignKey(Modulo, related_name='paquetes', blank=True, null=True)
	tipo_paquete = models.ForeignKey(TipoPaquete, related_name='paquetes')
	nombre_paquete = models.CharField('Nombre del paquete', max_length=35)
	descripcion_paquete = models.TextField('Descripción del paquete (opcional)', blank=True)
	path = models.CharField('Ruta del paquete', max_length=250, blank=True)

	def __unicode__(self):
		return self.nombre_paquete
