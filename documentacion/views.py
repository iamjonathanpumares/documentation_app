# -*- coding: utf-8 -*-
import json

from django.core.urlresolvers import reverse
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
		queryset = Modulo.objects.filter(proyecto__slug=slug, modulo_depende=None)
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
		queryset = Modulo.objects.filter(proyecto__slug=slug, modulo_depende__id=id)
		return queryset

	def get_context_data(self, **kwargs):
	    context = super(SubmoduloListView, self).get_context_data(**kwargs)
	    slug = self.kwargs['slug']
	    id = self.kwargs['id']
	    context['proyecto'] = get_object_or_404(Proyecto, slug=slug)
	    modulo_padre = get_object_or_404(Modulo, id=id)
	    context['modulo_padre'] = modulo_padre
	    #context['modulo_depende'] = modulo_padre.modulos_depende.all().order_by('nivel')
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

	if request.method == 'POST':
		if 'tipo_paquete_radio' in request.POST and 'tipo_agregar_paquete_radio' in request.POST:
			tipo_paquete_radio = request.POST['tipo_paquete_radio']
			tipo_agregar_paquete_radio = request.POST['tipo_agregar_paquete_radio']

			if tipo_agregar_paquete_radio == 'existente':
				paquete_requerido_id = request.POST['paquete']

				paquete_requerido_instance = Paquete.objects.get(pk=paquete_requerido_id)

				paquete_instance.paquetes_requeridos.add(paquete_requerido_instance)

					

			if tipo_agregar_paquete_radio == 'nuevo':

				form = PaqueteForm(request.POST)
				if form.is_valid():
					paquete = form.save(commit=False)
					paquete.proyecto = proyecto_instance
					if tipo_paquete_radio == 'si':
						ubicacion_paquete_radio = request.POST['ubicacion_paquete_radio']	

						if ubicacion_paquete_radio == 'modulo_principal':
							modulo_id = request.POST['modulo_principal']
						elif ubicacion_paquete_radio == 'submodulo':
							modulo_id = request.POST['submodulos_totales']

						modulo_instance = Modulo.objects.get(pk=modulo_id)
						
						paquete.modulo = modulo_instance
						paquete.path = '%s/%s' % (modulo_instance.path, paquete.nombre_paquete)
						
					paquete.save()
					paquete_instance.paquetes_requeridos.add(paquete)

			if 'save' in request.POST:
				return redirect(reverse('paquetes-modulo', kwargs={ 'slug': proyecto_instance.slug, 'id': paquete_instance.modulo.id }))
			elif 'add_another' in request.POST:
				return redirect(reverse('paquetes-requeridos', kwargs={ 'slug': proyecto_instance.slug, 'id': paquete_instance.id }))
	
	else:
		form = PaqueteForm()


	return render(request, 'documentacion/paquete_requerido_form.html', { 'proyecto': proyecto_instance, 'form': form })

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
				modulo.path = '%s/%s' % (modulo_padre_instance.path, modulo.nombre_modulo)
				modulo.modulo_depende = modulo_padre_instance

				ruta = modulo.path.split('/')
				modulo_principal_instance = Modulo.objects.get(proyecto__slug=ruta[0], nombre_modulo=ruta[1], modulo_depende=None)
				modulo.modulo_principal = modulo_principal_instance
				
				modulo.save()
				return redirect('/documentacion/submodulos/%s/%s/' % (proyecto_instance.slug, id))
			modulo.nivel = 1
			modulo.path = '%s/%s' % (proyecto_instance.slug, modulo.nombre_modulo)
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
