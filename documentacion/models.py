# -*- coding: utf-8 -*-
from django.db import models
from proyectos.models import Proyecto

class Modulo(models.Model):
	proyecto = models.ForeignKey(Proyecto, related_name='modulos')
	nombre_modulo = models.CharField('Nombre del módulo', max_length=35)
	descripcion_modulo = models.TextField('Descripción del módulo')

	def __unicode__(self):
		return self.nombre_modulo

class TipoPaquete(models.Model):
	clave_paquete = models.CharField('Clave del paquete', max_length=3, primary_key=True)
	tipo_paquete = models.CharField('Nombre del paquete', max_length=50)

class Paquete(models.Model):
	tipo_paquete = models.ForeignKey(TipoPaquete, related_name='paquetes')
	nombre_paquete = models.CharField('Nombre del paquete', max_length=50)
