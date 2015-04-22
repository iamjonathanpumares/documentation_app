import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView
from .models import Proyecto
from .serializers import ProyectoSerializer
from .forms import ProyectoCreateForm, ProyectoUpdateForm

"""class ProyectoCreateView(CreateView):
	model = Proyecto
	fields = ('nombre_proyecto', 'descripcion_proyecto', 'lenguajes_utilizados', 'bases_de_datos', 'frameworks_backend', 'frameworks_frontend', 'servidor_web', 'plugins_libs',)
	success_url = '/proyectos/'

	def get_context_data(self, **kwargs):
	    context = super(ProyectoCreateView, self).get_context_data(**kwargs)
	    context['action'] = 'create'
	    return context"""

def ProyectoCreateView(request):
	if request.method == 'POST':
		form = ProyectoCreateForm(request.POST)
		if form.is_valid():
			proyecto = form.save()
			return redirect('/proyectos/')
	else:
		form = ProyectoCreateForm()
	return render(request, 'proyectos/proyecto_form.html', { 'form': form, 'action': 'create' })

def ProyectoUpdateView(request, slug):
	proyecto_instance = get_object_or_404(Proyecto, slug=slug)
	nombre_proyecto_anterior = proyecto_instance.nombre_proyecto 
	if request.method == 'POST':
		form = ProyectoUpdateForm(request.POST, instance=proyecto_instance)
		if form.is_valid():
			modifico_nombre_proyecto = True if nombre_proyecto_anterior != form.cleaned_data['nombre_proyecto'] else False
			proyecto = form.save(modifico_nombre_proyecto=modifico_nombre_proyecto)
			return redirect('/proyectos/')
	else:
		form = ProyectoUpdateForm(instance=proyecto_instance)
	return render(request, 'proyectos/proyecto_form.html', { 'form': form, 'action': 'update' })

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
