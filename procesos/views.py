import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Max
from django.views.generic import ListView, TemplateView, View
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .forms import ProcesoForm
from .models import Actividad, Proceso, Responsable
from .serializers import ActividadSerializer
from proyectos.models import Proyecto

def ProcesoCreateView(request, slug):
	proyecto_instance = get_object_or_404(Proyecto, slug=slug)
	if request.method == 'POST':
		form = ProcesoForm(request.POST)
		if form.is_valid():
			proceso = form.save(commit=False)
			proceso.proyecto = proyecto_instance
			proceso.save()
			return redirect('/procesos/%s/' % proyecto_instance.slug)
	else:
		form = ProcesoForm()
	return render(request, 'procesos/proceso_form.html', { 'form': form, 'action': 'create' })

def ProcesoUpdateView(request, slug, id):
	proceso_instance = get_object_or_404(Proceso, proyecto__slug=slug, id=id)
	if request.method == 'POST':
		form = ProcesoForm(request.POST, instance=proceso_instance)
		if form.is_valid():
			proceso = form.save()
			return redirect('/procesos/%s/' % proceso_instance.proyecto.slug)
	else:
		form = ProcesoForm(instance=proceso_instance)
	return render(request, 'Procesos/Proceso_form.html', { 'form': form, 'action': 'update' })

@api_view(['GET', 'POST'])
def ActividadAPIView(request):
	if request.method == 'GET':
		actividades = Actividad.objects.all()
		serializer = ActividadSerializer(actividades, many=True)
		return Response(serializer.data)


	if request.method == 'POST':
		serializer = ActividadSerializer(data=request.data)
		if serializer.is_valid():
			actividad = serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProcesoListView(ListView):
	model = Proceso

	def post(self, request, *args, **kwargs):
		# Elimina un proceso en la lista
		if 'proceso' in request.POST:
			id_proceso = request.POST['proceso']
			try:
				object = Proceso.objects.get(pk=id_proceso)
				mensaje = { "status": "True", "id": object.id, "action": "Eliminar" }
				object.delete()
				return HttpResponse(json.dumps(mensaje))
			except:
				mensaje = { "status": "False", "action": "Eliminar" }
				return HttpResponse(json.dumps(mensaje))

	def get_queryset(self, *args, **kwargs):
		slug = self.kwargs['slug']
		procesos = Proceso.objects.filter(proyecto__slug=slug).order_by('nombre_proceso')
		return procesos

	def get_context_data(self, **kwargs):
	    context = super(ProcesoListView, self).get_context_data(**kwargs)
	    slug = self.kwargs['slug']
	    context['proyecto'] = get_object_or_404(Proyecto, slug=slug)
	    return context

def ProcesoDetailView(request, id):
	template_name = 'procesos/proceso_detail.html'
	context = {}

	proceso = get_object_or_404(Proceso, id=id)
	context['proceso'] = proceso

	responsables = Responsable.objects.filter(proceso__id=id)
	context['responsables'] = responsables

	orden = proceso.actividades.all().aggregate(Max('orden'))
	if not orden['orden__max']:
		context['orden_max'] = 1
	else:
		context['orden_max'] = orden['orden__max'] + 1

	context['actividades'] = proceso.actividades.all().order_by('orden')
    
	if request.method == 'POST':
		# Elimina un responsable en la lista
		if 'responsable' in request.POST:
			id_responsable = request.POST['responsable']

			object = get_object_or_404(Responsable, pk=id_responsable)
			object.delete()
			return redirect(reverse('proceso-detail', kwargs={ 'id': id }))
	return render(request, template_name, context)
			

