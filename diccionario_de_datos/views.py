# -*- coding: utf-8 -*-
import json
# Libreria para hacer debug y ver el contenido de nuestras variables
# import pdb

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from proyectos.models import Proyecto

from .models import Tabla, Relacion
from .forms import TablaForm, CampoForm

""" 
	Dos maneras de guardar llaves foraneas a los campos de nuestro modelo

	instancia.campoforaneo = instancia_referencia
	instancia.campoforaneo_id = valor_numerico
"""

def TablaListView(request, slug):
	proyecto = get_object_or_404(Proyecto, slug=slug)
	tablas = Tabla.objects.filter(proyecto__slug=slug).order_by('nombre_tabla')

	if request.method == 'POST':
		# Elimina un tabla en la lista
		if 'tabla' in request.POST:
			id_tabla = request.POST['tabla']
			try:
				object = Tabla.objects.get(pk=id_tabla)
				mensaje = { "status": "True", "id": object.id, "action": "Eliminar" }
				object.delete()
				return HttpResponse(json.dumps(mensaje))
			except:
				mensaje = { "status": "False", "action": "Eliminar" }
				return HttpResponse(json.dumps(mensaje))

	return render(request, 'diccionario_de_datos/tabla_list.html', { 'proyecto': proyecto, 'tablas': tablas })

def TablaCreateView(request, slug, id=None):
	action = 'create'
	proyecto = get_object_or_404(Proyecto, slug=slug)
	if id:
		tabla_instance = get_object_or_404(Tabla, id=id, proyecto__slug=slug)
		action = 'update'

	if request.method == 'POST':
		if id:
			form = TablaForm(request.POST, instance=tabla_instance)
			if form.is_valid():
				tabla = form.save()
				return redirect(reverse('tablas-list', kwargs={ 'slug': proyecto.slug }))
		else:
			form = TablaForm(request.POST)
			if form.is_valid():
				tabla = form.save(commit=False)
				tabla.proyecto = proyecto
				tabla.save()
				return redirect(reverse('tablas-list', kwargs={ 'slug': proyecto.slug }))
	else:
		if id:
			form = TablaForm(instance=tabla_instance)
		else:
			form = TablaForm()
	return render(request, 'diccionario_de_datos/tabla_form.html', { 'proyecto': proyecto, 'form': form, 'action': action })

def CampoListView(request, slug, id):
	proyecto = get_object_or_404(Proyecto, slug=slug)
	tabla = get_object_or_404(Tabla, id=id, proyecto__slug=slug)
	campos = tabla.campos.all().order_by('id')
	campos_clave = tabla.campos.filter(campo_clave=True).order_by('id')
	relaciones = []
	cont = 0

	for campo_clave in campos_clave:
		try:
			relacion = Relacion.objects.filter(campo__id=campo_clave.id)
			relaciones.append(relacion)
		except:
			pass

	# Método para detener y visualizar el contenido de las variables (Debug)		
	# pdb.set_trace()

	if request.method == 'POST':
		pass
	else:
		form = CampoForm()
	return render(request, 'diccionario_de_datos/campo_list.html', { 'proyecto': proyecto, 'tabla': tabla, 'campos': campos, 'campos_clave': campos_clave, 'form': form, 'relaciones': relaciones })
