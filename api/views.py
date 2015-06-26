from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from proyectos.models import Proyecto
from procesos.models import Proceso
from proyectos.serializers import ProyectoSerializer
from .serializers import PaqueteSerializer
from . import serializers

class ProyectoListAPIView(generics.ListAPIView):
	queryset = Proyecto.objects.all()
	serializer_class = ProyectoSerializer

class ProyectoDetailAPIView(generics.RetrieveAPIView):
	queryset = Proyecto.objects.all()
	serializer_class = ProyectoSerializer

class ProcesoDetailAPIView(generics.RetrieveAPIView):
	queryset = Proceso.objects.all()
	serializer_class = serializers.ProcesoSerializer

@api_view(['POST'])
def PaqueteCreateAPIView(request):
	if request.method == 'POST':
		serializer = PaqueteSerializer(data=request.data)
		if serializer.is_valid():
			actividad = serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
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
