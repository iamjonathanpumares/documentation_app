from .models import Proyecto
from rest_framework import serializers

class ProyectoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Proyecto