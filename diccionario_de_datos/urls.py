# -*- coding: utf-8 -*-
from django.urls import re_path
from . import views

urlpatterns = [
	#url(r'^(?P<slug>[\w\-]+)/$', views.ModuloListView.as_view()),
	re_path(r'^tablas/(?P<slug>[\w\-]+)/$', views.TablaListView, name='tablas-list'),
	re_path(r'^tablas/(?P<slug>[\w\-]+)/add/$', views.TablaCreateView, name='tabla-create'),
	re_path(r'^tablas/(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/$', views.TablaCreateView, name='tabla-update'),
	re_path(r'^tablas/(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/campos/$', views.CampoListView, name='campos-list'),
	#url(r'^tablas/(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/$', views.ActorDetailView, name='actor-detail'),
]