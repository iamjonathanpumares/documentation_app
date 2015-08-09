from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect

from proyectos.models import Proyecto

from .forms import ActorForm
from .models import Actor

def ActorListView(request, slug):
	proyecto = get_object_or_404(Proyecto, slug=slug)
	actores = Actor.objects.filter(proyecto__slug=slug)
	return render(request, 'casos_de_uso/actor_list.html', { 'proyecto': proyecto, 'actores': actores })

def ActorDetailView(request, slug, id):
	proyecto = get_object_or_404(Proyecto, slug=slug)
	actor = Actor.objects.get(proyecto__slug=slug, id=id)
	tareas = actor.tareas.all()
	cont = 1
	return render(request, 'casos_de_uso/actor_detail.html', { 'proyecto': proyecto, 'actor': actor, 'tareas': tareas, 'cont': cont })

def ActorCreateView(request, slug):
	proyecto = get_object_or_404(Proyecto, slug=slug)
	if request.method == 'POST':
		form = ActorForm(request.POST)
		if form.is_valid():
			actor = form.save(commit=False)
			actor.proyecto = proyecto
			actor.save()
			return redirect(reverse('actores-list', kwargs={ 'slug': proyecto.slug }))
	else:
		form = ActorForm()
	return render(request, 'casos_de_uso/actor_form.html', { 'form': form, 'action': 'create' })