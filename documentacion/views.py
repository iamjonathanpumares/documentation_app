# -*- coding: utf-8 -*-
import json

from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Modulo, Paquete, TipoPaquete
from .forms import ModuloForm, PaqueteForm
from proyectos.models import Proyecto

class ModuloListView(ListView):
	model = Modulo

	def get_queryset(self):
		slug = self.kwargs['slug']
		queryset = Modulo.objects.filter(proyecto__slug=slug, modulo_depende=None).order_by('nombre_modulo')
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
		queryset = Modulo.objects.filter(proyecto__slug=slug, modulo_depende__id=id).order_by('nombre_modulo')
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
		name = self.request.GET.get('q', '')
		if (name != ''):
			object_list = Paquete.objects.filter(modulo__proyecto__slug=slug, modulo__id=id, tipo_paquete__clave_paquete=name).order_by('nombre_paquete')
			self.paginate_by = None
		else:
			object_list = Paquete.objects.filter(modulo__proyecto__slug=slug, modulo__id=id).order_by('nombre_paquete')
			self.paginate_by = 15
		return object_list

		"""queryset = Paquete.objects.filter(modulo__proyecto__slug=slug, modulo__id=id)
		return queryset"""

	def get_context_data(self, **kwargs):
		# Entrada
	    context = super(PaqueteListView, self).get_context_data(**kwargs)
	    slug = self.kwargs['slug']
	    id = self.kwargs['id']
	    q = self.request.GET.get('q', '')

	    # Proceso
	    proyecto = get_object_or_404(Proyecto, slug=slug)
	    modulo = get_object_or_404(Modulo, id=id)
	    no_paquetes = Paquete.objects.filter(modulo__proyecto__slug=slug, modulo__id=id).count()
	    tipos_paquetes = TipoPaquete.objects.filter(paquetes__modulo__proyecto__slug=slug, paquetes__modulo__id=id).distinct()
	    context['proyecto'] = proyecto
	    context['modulo'] = modulo
	    context['no_submodulos'] = modulo.submodulos.all().count()
	    context['no_paquetes'] = no_paquetes
	    context['tipos_paquetes'] = tipos_paquetes
	    context['q'] = q
	    context['form'] = PaqueteForm()

	    # Salida
	    return context

	def post(self, request, *args, **kwargs):
		# Elimina un proyecto en la lista
		if 'paquete_delete' in request.POST:
			try:
				id_paquete = request.POST['paquete_delete']
				paquete = Paquete.objects.get(pk=id_paquete)
				mensaje = { "status": "True" }
				paquete.delete()
				return HttpResponse(json.dumps(mensaje))
			except:
				mensaje = { "status": "False", "action": "Eliminar" }
				return HttpResponse(json.dumps(mensaje))
		else:		
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
				return redirect('paquetes-requeridos-list', kwargs={ 'slug': proyecto_instance.slug, 'id': paquete_instance.id })
			elif 'add_another' in request.POST:
				return redirect('paquetes-requeridos', kwargs={ 'slug': proyecto_instance.slug, 'id': paquete_instance.id })
	
	else:
		form = PaqueteForm()


	return render(request, 'documentacion/paquete_requerido_form.html', { 'proyecto': proyecto_instance, 'paquete': paquete_instance, 'form': form })

def PaqueteRequeridoListView(request, slug, id):
	proyecto = get_object_or_404(Proyecto, slug=slug)
	paquete = get_object_or_404(Paquete, pk=id)
	paquetes_modulos = paquete.paquetes_requeridos.exclude(modulo=None).order_by('nombre_paquete')
	paquetes_independientes = paquete.paquetes_requeridos.filter(modulo=None).order_by('nombre_paquete')

	if request.method == 'POST':
		if 'paquete' in request.POST:
			try:
				id_paquete = request.POST['paquete']
				paquete_requerido = Paquete.objects.get(pk=id_paquete)
				paquete.paquetes_requeridos.remove(paquete_requerido)
				return redirect('paquetes-requeridos-list', kwargs={ 'slug': proyecto.slug, 'id': paquete.id })
			except:
				mensaje = { "status": "False" }
				return HttpResponse(json.dumps(mensaje))

	return render(request, 'documentacion/paquete_requerido_list.html', { 'proyecto': proyecto, 'paquete': paquete, 'paquetes_modulos': paquetes_modulos, 'paquetes_independientes': paquetes_independientes })

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
