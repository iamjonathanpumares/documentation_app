# -*- coding: utf-8 -*-
# Imports propios de Python

# Imports módulos de terceros (Paquetes instalados con PIP) 
from django.db import models

# Imports propios de la aplicación
from proyectos.models import Proyecto

class Actor(models.Model):
	proyecto = models.ForeignKey(Proyecto, related_name='actores')
	# Un actor es un rol que un usuario juega con respecto al sistema, es una entidad externa (personas, sistemas externos) que interactua con el sistema.
	rol = models.CharField('Rol del actor', max_length=50, help_text='Un rol son los distintos usuarios que interactuan con el sistema. Ejemplo: Gerente de ventas, el cliente, proveedor, empleado, recepcionista, etc.')

class Tarea(models.Model):
	actor = models.ForeignKey(Actor, related_name='tareas')
	descripcion = models.TextField('Descripción de la tarea o actividad que realiza el actor')