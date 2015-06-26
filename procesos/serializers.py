from rest_framework import serializers
from .models import Actividad

class ActividadSerializer(serializers.ModelSerializer):

	class Meta:
		model = Actividad
		fields = ('proceso', 'nombre_actividad', 'tipo_actividad', 'orden',)