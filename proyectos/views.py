import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView
from .models import Proyecto
from .serializers import ProyectoSerializer

class ProyectoCreateView(CreateView):
	model = Proyecto
	fields = ('nombre_proyecto', 'descripcion_proyecto', 'lenguajes_utilizados', 'bases_de_datos', 'frameworks_backend', 'frameworks_frontend', 'servidor_web', 'plugins_libs',)
	success_url = '/proyectos/'

	def get_context_data(self, **kwargs):
	    context = super(ProyectoCreateView, self).get_context_data(**kwargs)
	    context['action'] = 'create'
	    return context

class HomeTemplateView(TemplateView):
	template_name = 'proyectos/home.html'

class ProyectoListView(ListView):
	model = Proyecto

	def post(self, request, *args, **kwargs):
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
				return HttpResponse(json.dumps(mensaje))

class ProyectoDetailView(UpdateView):
	model = Proyecto
	fields = ('nombre_proyecto', 'descripcion_proyecto', 'lenguajes_utilizados', 'bases_de_datos', 'frameworks_backend', 'frameworks_frontend', 'servidor_web', 'plugins_libs',)
	success_url = '/proyectos/'

	def get_context_data(self, **kwargs):
	    context = super(ProyectoDetailView, self).get_context_data(**kwargs)
	    context['action'] = 'update'
	    return context

"""from rest_framework import generics

class ProyectoCreateView(generics.CreateAPIView):
	queryset = Proyecto.objects.all()
	serializer_class = ProyectoSerializer"""
