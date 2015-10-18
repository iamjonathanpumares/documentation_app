# -*- coding: utf-8 -*-
from django.db import models

from proyectos.models import Proyecto

class Tabla(models.Model):
	proyecto = models.ForeignKey(Proyecto, related_name='tablas')
	nombre_tabla = models.CharField('Nombre de la tabla', max_length=35)
	descripcion_tabla = models.CharField('Descripción de la tabla', max_length=150)
	fecha_creacion = models.DateField('Fecha de creación', auto_now=True)

	def __unicode__(self):
		return self.nombre_tabla

class Campo(models.Model):
	tabla = models.ForeignKey(Tabla, related_name='campos')
	tipo_dato = models.ForeignKey('TipoDato', related_name='campos')
	campo = models.CharField('Campo de la tabla', max_length=35)
	longitud = models.PositiveSmallIntegerField('Longitud del campo', blank=True, null=True)
	descripcion = models.CharField('Descripción del campo', max_length=100)
	campo_clave = models.BooleanField('Campo clave')

	def __unicode__(self):
		return self.campo

class TipoDato(models.Model):
	tipo = models.CharField('Tipo de dato', max_length=40)

	def __unicode__(self):
		return self.tipo

class Relacion(models.Model):
	campo = models.ForeignKey(Campo, related_name='relaciones')
	tabla_referencia = models.ForeignKey(Tabla, related_name='relaciones')

	def __unicode__(self):
		return '%s - %s' % (self.campo.campo, self.tabla_referencia.nombre_tabla)
