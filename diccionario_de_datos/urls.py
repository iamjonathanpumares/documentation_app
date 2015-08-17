# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	#url(r'^(?P<slug>[\w\-]+)/$', views.ModuloListView.as_view()),
	url(r'^tablas/(?P<slug>[\w\-]+)/$', views.TablaListView, name='tablas-list'),
	url(r'^tablas/(?P<slug>[\w\-]+)/add/$', views.TablaCreateView, name='tabla-create'),
	url(r'^tablas/(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/$', views.TablaCreateView, name='tabla-update'),
	#url(r'^tablas/(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/$', views.ActorDetailView, name='actor-detail'),
)