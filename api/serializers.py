from rest_framework import serializers
from proyectos.models import Proyecto
from procesos.models import Proceso, Actividad
from documentacion.models import Paquete, TipoPaquete

class ProyectoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Proyecto

class ActividadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Actividad
		fields = ('nombre_actividad', 'orden',)

class ProcesoSerializer(serializers.ModelSerializer):
	actividades = ActividadSerializer(many=True, read_only=True)

	class Meta:
		model = Proceso
		fields = ('nombre_proceso', 'descripcion_proceso', 'actividades',)

class TipoPaqueteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Paquete
		fields = ('clave_paquete', 'tipo_paquete',)

class PaqueteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Paquete
		fields = ('modulo', 'tipo_paquete', 'nombre_paquete', 'descripcion_paquete',)