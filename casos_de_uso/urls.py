# -*- coding: utf-8 -*-
from django.urls import re_path
from . import views

urlpatterns = [
	#url(r'^(?P<slug>[\w\-]+)/$', views.ModuloListView.as_view()),
	re_path(r'^actores/(?P<slug>[\w\-]+)/$', views.ActorListView, name='actores-list'),
	re_path(r'^actores/(?P<slug>[\w\-]+)/add/$', views.ActorCreateView, name='actor-create'),
	re_path(r'^actores/(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/$', views.ActorDetailView, name='actor-detail'),
]