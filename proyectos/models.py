# -*- coding: utf-8 -*-
from django.db import models

class Proyecto(models.Model):
	#slug = models.SlugField('Slug para las URLs de los proyectos', unique=True)
	nombre_proyecto = models.CharField('Nombre del proyecto', max_length=50)
	descripcion_proyecto = models.TextField('Descripción del proyecto')
	lenguajes_utilizados = models.CharField('Lenguajes utilizados en el proyecto', max_length=80, help_text='Ejemplo: Python, Javascript, Ruby, etc.')
	bases_de_datos = models.CharField('Bases de datos utilizadas en el proyecto', max_length=80, help_text='Ejemplo: MySQL, PostgreSQL, MongoDB, etc.')
	frameworks_backend = models.CharField('Frameworks Backend utilizados en el proyecto', max_length=80, blank=True, help_text='Ejemplo: Django, Sails.js, Rails, etc.')
	frameworks_frontend = models.CharField('Frameworks Frontend utilizados en el proyecto', max_length=80, blank=True, help_text='Ejemplo: Angular.js, Backbone.js, Bootstrap, etc.')
	servidor_web = models.CharField('Servidor web en el corre el proyecto', max_length=50, blank=True, help_text='Ejemplo: Apache, Nginx, Unicorn, Tomcat, Gunicorn, etc.')
	plugins_libs = models.TextField('Plugins y librerías utilizadas en el proyecto', blank=True, help_text='Ejemplo: jQuery, React.js, Fancybox, jQuery UI, etc.')
	fecha_creacion = models.DateField('Fecha de creación', auto_now=True)

	def __unicode__(self):
		return self.nombre_proyecto



