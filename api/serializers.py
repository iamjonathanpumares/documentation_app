from rest_framework import serializers
from proyectos.models import Proyecto
from procesos.models import Proceso, Actividad
from documentacion.models import Paquete, TipoPaquete, Modulo

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
		model = TipoPaquete
		fields = ('clave_paquete', 'tipo_paquete',)

class PaqueteRequeridoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Paquete
		fields = ('paquetes_requeridos',)

class PaqueteSerializer(serializers.ModelSerializer):
	#tipo_paquete = TipoPaqueteSerializer()

	class Meta:
		model = Paquete
		fields = ('id', 'proyecto', 'modulo', 'tipo_paquete', 'nombre_paquete', 'descripcion_paquete',)

class ModuloDetailSerializer(serializers.ModelSerializer):
	paquetes = PaqueteSerializer(many=True, read_only=True)

	class Meta:
		model = Modulo
		fields = ('id', 'nombre_modulo', 'descripcion_modulo', 'nivel', 'path', 'paquetes',)

# ----------------------------------------------------------------------------------
class ModuloSerializer(serializers.ModelSerializer):

	class Meta:
		model = Modulo
		fields = ('id', 'nombre_modulo', 'descripcion_modulo', 'nivel', 'path',)

class SubmoduloTotalesSerializer(serializers.ModelSerializer):
	submodulos_totales = ModuloSerializer(many=True, read_only=True)

	class Meta:
		model = Modulo
		fields = ('nombre_modulo', 'submodulos_totales',)