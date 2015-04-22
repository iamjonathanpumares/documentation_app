import itertools
from django import forms
from django.utils.text import slugify
from .models import Proyecto

# Formulario para crear un proyecto nuevo
class ProyectoCreateForm(forms.ModelForm):
	class Meta:
		model = Proyecto
		fields = ('nombre_proyecto', 'descripcion_proyecto', 'lenguajes_utilizados', 'bases_de_datos', 'frameworks_backend', 'frameworks_frontend', 'servidor_web', 'plugins_libs',)

	def save(self):
		proyecto = super(ProyectoCreateForm, self).save(commit=False)
		proyecto.slug = orig = slugify(proyecto.nombre_proyecto)

		for x in itertools.count(1):
			if not Proyecto.objects.filter(slug=proyecto.slug).exists():
				break
			proyecto.slug = '%s-%d' % (orig, x)

		proyecto.save()

		return proyecto

# Formulario para actualizar un proyecto existente
class ProyectoUpdateForm(forms.ModelForm):
	class Meta:
		model = Proyecto
		fields = ('nombre_proyecto', 'descripcion_proyecto', 'lenguajes_utilizados', 'bases_de_datos', 'frameworks_backend', 'frameworks_frontend', 'servidor_web', 'plugins_libs',)

	def save(self, *args, **kwargs):
		proyecto = super(ProyectoUpdateForm, self).save(commit=False)
		modifico = kwargs['modifico_nombre_proyecto']

		if modifico:
			proyecto.slug = orig = slugify(proyecto.nombre_proyecto)

			for x in itertools.count(1):
				if not Proyecto.objects.filter(slug=proyecto.slug).exists():
					break
				proyecto.slug = '%s-%d' % (orig, x)

			proyecto.save()

			return proyecto
		proyecto.save()
		return proyecto

