from django import forms
from .models import Proceso, Actividad

class ProcesoForm(forms.ModelForm):
	class Meta:
		model = Proceso
		fields = ('nombre_proceso', 'descripcion_proceso',)

class ActividadForm(forms.ModelForm):
	class Meta:
		model = Actividad
		fields = ('nombre_actividad',)