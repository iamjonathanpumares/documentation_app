from django import forms

from .models import Tabla

class TablaForm(forms.ModelForm):
	class Meta:
		model = Tabla
		fields = ('nombre_tabla', 'descripcion_tabla',)