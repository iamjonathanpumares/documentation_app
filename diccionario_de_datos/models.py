# -*- coding: utf-8 -*-
from django.db import models

from proyectos.models import Proyecto

class Tabla(models.Model):
	proyecto = models.ForeignKey(Proyecto, related_name='tablas')
	nombre_tabla = models.CharField('Nombre de la tabla', max_length=35)
	descripcion_tabla = models.CharField('Descripción de la tabla', max_length=150)
	fecha_creacion = models.DateField('Fecha de creación', auto_now=True)

class Campo(models.Model):
	tabla = models.ForeignKey(Tabla, related_name='campos')
	campo = models.CharField('Campo de la tabla', max_length=35)
	longitud = models.PositiveSmallIntegerField('Longitud del campo')
	tipo_dato = models.CharField('Tipo de dato del campo', max_length=35)
	descripcion = models.CharField('Descripción del campo', max_length=100)
	campo_clave = models.BooleanField('Campo clave')

class Relacion(models.Model):
	campo = models.ForeignKey(Campo, related_name='relaciones')
	tabla_referencia = models.ForeignKey(Tabla, related_name='relaciones')
