# -*- coding: utf-8 -*-
import json
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Modulo, Paquete
from .forms import ModuloForm, PaqueteForm
from proyectos.models import Proyecto

class ModuloListView(ListView):
	model = Modulo

	def get_queryset(self):
		slug = self.kwargs['slug']
		queryset = Modulo.objects.filter(proyecto__slug=slug, modulos_depende=None)
		return queryset

	def get_context_data(self, **kwargs):
	    context = super(ModuloListView, self).get_context_data(**kwargs)
	    slug = self.kwargs['slug']
	    context['proyecto'] = get_object_or_404(Proyecto, slug=slug)
	    return context

	def post(self, request, *args, **kwargs):
		# Elimina un proyecto en la lista
		if 'proyecto_id' in request.POST:
			try:
				id_proyecto = request.POST['proyecto_id']
				proyecto = Modulo.objects.get(pk=id_proyecto)
				mensaje = { "status": "True", "proyecto_id": proyecto.id, "action": "Eliminar" }
				proyecto.delete()
				return HttpResponse(json.dumps(mensaje))
			except:
				mensaje = { "status": "False", "action": "Eliminar" }
				return HttpResponse(json.dumps(mensaje))

class SubmoduloListView(ListView):
	model = Modulo
	template_name = 'documentacion/submodulo_list.html'

	def get_queryset(self):
		slug = self.kwargs['slug']
		id = self.kwargs['id']
		queryset = Modulo.objects.filter(proyecto__slug=slug, modulos_depende__id=id)
		return queryset

	def get_context_data(self, **kwargs):
	    context = super(SubmoduloListView, self).get_context_data(**kwargs)
	    slug = self.kwargs['slug']
	    id = self.kwargs['id']
	    context['proyecto'] = get_object_or_404(Proyecto, slug=slug)
	    modulo_padre = get_object_or_404(Modulo, id=id)
	    context['modulo_padre'] = modulo_padre
	    context['modulos_depende'] = modulo_padre.modulos_depende.all().order_by('nivel')
	    return context

class PaqueteListView(ListView):
	model = Paquete

	def get_queryset(self):
		slug = self.kwargs['slug']
		id = self.kwargs['id']
		queryset = Paquete.objects.filter(modulo__proyecto__slug=slug, modulo__id=id)
		return queryset

	def get_context_data(self, **kwargs):
		# Entrada
	    context = super(PaqueteListView, self).get_context_data(**kwargs)
	    slug = self.kwargs['slug']
	    id = self.kwargs['id']

	    # Proceso
	    context['proyecto'] = get_object_or_404(Proyecto, slug=slug)
	    context['modulo'] = get_object_or_404(Modulo, id=id)
	    context['form'] = PaqueteForm()

	    # Salida
	    return context

	def post(self, request, *args, **kwargs):
		form = PaqueteForm(request.POST)
		if form.is_valid():
			paquete = form.save(commit=False)

def PaqueteRequeridoView(request, slug, id):
	proyecto_instance = Proyecto.objects.get(slug=slug)
	paquete_instance = Paquete.objects.get(pk=id)
	modulos = Modulo.objects.filter(proyecto__slug=slug, modulos_depende=None)

	modulos_list = []
	for modulo in modulos:
		modulo_dict = { 'modulo': modulo, 'submodulos': modulo.submodulos.all().order_by('nivel') }
		modulos_list.append(modulo_dict)


	return render(request, 'documentacion/paquete_requerido_form.html', { 'modulos': modulos_list })

# 1. Guardar el módulo padre en el campo modulos_depende
# 2. Guardar los módulos de los que depende su padre por medio de un for
# 3. Checar el nivel que tiene su padre y ponerle uno más
def ModuloCreateView(request, slug, id=None):
	proyecto_instance = get_object_or_404(Proyecto, slug=slug)
	if request.method == 'POST':
		form = ModuloForm(request.POST)
		if form.is_valid():
			modulo = form.save(commit=False)
			modulo.proyecto = proyecto_instance
			if id:	
				modulo_padre_instance = get_object_or_404(Modulo, id=id)
				modulo.nivel = modulo_padre_instance.nivel + 1
				modulo.save()
				modulo.modulos_depende.add(modulo_padre_instance)
				for modulo_depende_padre in modulo_padre_instance.modulos_depende.all():
					modulo.modulos_depende.add(modulo_depende_padre)
				return redirect('/documentacion/submodulos/%s/%s/' % (proyecto_instance.slug, id))
			modulo.nivel = 1
			modulo.save()
			return redirect('/documentacion/%s/' % proyecto_instance.slug)
	else:
		form = ModuloForm()
	return render(request, 'documentacion/modulo_form.html', { 'proyecto': proyecto_instance, 'form': form, 'action': 'create' })

def ModuloUpdateView(request, slug, id):
	proyecto_instance = get_object_or_404(Proyecto, slug=slug)
	modulo_instance = get_object_or_404(Modulo, proyecto__slug=slug, id=id)
	if request.method == 'POST':
		form = ModuloForm(request.POST, instance=modulo_instance)
		if form.is_valid():
			modulo = form.save()
			return redirect('/documentacion/%s/' % modulo_instance.proyecto.slug)
	else:
		form = ModuloForm(instance=modulo_instance)
	return render(request, 'documentacion/modulo_form.html', { 'proyecto': proyecto_instance, 'form': form, 'action': 'update' })

	"""def post(self, request, *args, **kwargs):
		# Elimina un proyecto en la lista
		if 'proyecto_id' in request.POST:
			try:
				id_proyecto = request.POST['proyecto_id']
				proyecto = Proyecto.objects.get(pk=id_proyecto)
				mensaje = { "status": "True", "proyecto_id": proyecto.id, "action": "Eliminar" }
				proyecto.delete()
				return HttpResponse(json.dumps(mensaje))
			except:
				mensaje = { "status": "False", "action": "Eliminar" }
				return HttpResponse(json.dumps(mensaje))"""
