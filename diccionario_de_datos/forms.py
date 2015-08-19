from django import forms

from .models import Tabla, Campo

class TablaForm(forms.ModelForm):
	class Meta:
		model = Tabla
		fields = ('nombre_tabla', 'descripcion_tabla',)

class CampoForm(forms.ModelForm):
	class Meta:
		model = Campo
		fields = ('campo', 'longitud', 'tipo_dato', 'descripcion',)