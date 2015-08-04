from django.shortcuts import render

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from proyectos.models import Proyecto
from documentacion.models import Modulo, Paquete, TipoPaquete
from procesos.models import Proceso
from proyectos.serializers import ProyectoSerializer

#from .serializers import PaqueteSerializer, SubmoduloTotalesSerializer, ModuloSerializer
from . import serializers

class ProyectoListAPIView(generics.ListAPIView):
	queryset = Proyecto.objects.all()
	serializer_class = ProyectoSerializer

class TipoPaqueteListAPIView(generics.ListAPIView):
	queryset = TipoPaquete.objects.all()
	serializer_class = serializers.TipoPaqueteSerializer

	def get_queryset(self):
		slug = self.kwargs['slug']
		queryset = TipoPaquete.objects.filter(paquetes__proyecto__slug=slug, paquetes__modulo=None)
		if not queryset:
			return Response(status=status.HTTP_404_NOT_FOUND)
		return queryset

class PaqueteListAPIView(generics.ListAPIView):
	queryset = Paquete.objects.all()
	serializer_class = serializers.PaqueteSerializer

	def get_queryset(self):
		slug = self.kwargs['slug']
		clave_paquete = self.kwargs['clave_paquete']
		queryset = Paquete.objects.filter(proyecto__slug=slug, modulo=None, tipo_paquete__clave_paquete=clave_paquete)
		if not queryset:
			return Response(status=status.HTTP_404_NOT_FOUND)
		return queryset

class PaqueteDetailAPIView(generics.DestroyAPIView):
	queryset = Paquete.objects.all()
	serializer_class = serializers.PaqueteSerializer

class ModulosPrincipalesListAPIView(generics.ListAPIView):
	queryset = Modulo.objects.filter(modulo_depende=None)
	serializer_class = serializers.ModuloSerializer

	def get_queryset(self):
		slug = self.kwargs['slug']
		queryset = Modulo.objects.filter(proyecto__slug=slug, modulo_depende=None)
		if not queryset:
			return Response(status=status.HTTP_404_NOT_FOUND)
		return queryset

class SubmodulosTotalesDetailAPIView(generics.RetrieveAPIView):
	queryset = Modulo.objects.filter(modulo_depende=None)
	serializer_class = serializers.SubmoduloTotalesSerializer
	ordering_fields = ('submodulos_totales__nivel',)

class ModuloDetailAPIView(generics.RetrieveAPIView):
	queryset = Modulo.objects.all()
	serializer_class = serializers.ModuloDetailSerializer

class ProyectoDetailAPIView(generics.RetrieveAPIView):
	queryset = Proyecto.objects.all()
	serializer_class = ProyectoSerializer

class ProcesoDetailAPIView(generics.RetrieveAPIView):
	queryset = Proceso.objects.all()
	serializer_class = serializers.ProcesoSerializer

@api_view(['POST'])
def PaqueteCreateAPIView(request):
	if request.method == 'POST':
		serializer = serializers.PaqueteSerializer(data=request.data)
		if serializer.is_valid():
			paquete = serializer.save()
			paquete.path = '%s/%s' % (paquete.modulo.path, paquete.nombre_paquete)
			paquete.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def PaqueteRequeridoCreateAPIView(request, pk):
	try:
		paquete_instance = Paquete.objects.get(pk=pk)
	except Paquete.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'PUT':
		serializer = serializers.PaqueteRequeridoSerializer(paquete_instance, data=request.data)
		if serializer.is_valid():
			id_paquetes_requeridos = request.data['paquetes_requeridos']
			paquete_requerido_instance = Paquete.objects.get(pk=id_paquetes_requeridos)
			paquete_instance.paquetes_requeridos.add(paquete_requerido_instance)
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""@api_view(['GET', 'POST'])
def ProcesoDetailAPIView(request, id):
	try:
		proceso = Proceso.objects.get(id=id)
	except Proceso.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		actividades = Actividad.objects.all()
		serializer = ActividadSerializer(actividades, many=True)
		return Response(serializer.data)


	if request.method == 'POST':
		serializer = ActividadSerializer(data=request.data)
		if serializer.is_valid():
			actividad = serializer.save(commit=False)"""
