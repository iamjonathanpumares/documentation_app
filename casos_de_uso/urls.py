# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	#url(r'^(?P<slug>[\w\-]+)/$', views.ModuloListView.as_view()),
	url(r'^actores/(?P<slug>[\w\-]+)/$', views.ActorListView, name='actores-list'),
	url(r'^actores/(?P<slug>[\w\-]+)/add/$', views.ActorCreateView, name='actor-create'),
	url(r'^actores/(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/$', views.ActorDetailView, name='actor-detail'),
)