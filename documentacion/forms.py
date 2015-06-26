from django import forms
from documentacion.models import Modulo, Paquete

class ModuloForm(forms.ModelForm):
	class Meta:
		model = Modulo
		fields = ('nombre_modulo', 'descripcion_modulo',)

class PaqueteForm(forms.ModelForm):
	class Meta:
		model = Paquete
		fields = ('nombre_paquete', 'tipo_paquete', 'descripcion_paquete',)