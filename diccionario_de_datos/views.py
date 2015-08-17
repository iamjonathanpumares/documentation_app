import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from proyectos.models import Proyecto

from .models import Tabla
from .forms import TablaForm

""" 
	Dos maneras de guardar llaves foraneas a los campos de nuestro modelo

	instancia.campoforaneo = instancia_referencia
	instancia.campoforaneo_id = valor_numerico
"""

def TablaListView(request, slug):
	proyecto = get_object_or_404(Proyecto, slug=slug)
	tablas = Tabla.objects.filter(proyecto__slug=slug)

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
