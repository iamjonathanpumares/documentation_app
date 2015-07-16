# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^(?P<slug>[\w\-]+)/$', views.ModuloListView.as_view()),
	url(r'^paquetes/(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/$', views.PaqueteListView.as_view(), name='paquetes-modulo'),
	url(r'^paquetes-requeridos/(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/$', views.PaqueteRequeridoView, name='paquetes-requeridos'),
	url(r'^submodulos/(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/$', views.SubmoduloListView.as_view()),
	url(r'^submodulos/(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/add/$', views.ModuloCreateView),
	url(r'^(?P<slug>[\w\-]+)/add/$', views.ModuloCreateView),
	url(r'^(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/$', views.ModuloUpdateView),
	#url(r'^(?P<pk>[0-9]+)/$', ProyectoDetailView.as_view()),
    #url(r'^create/$', ProyectoCreateView.as_view()),
    #url(r'^home/$', HomeTemplateView.as_view()),
    
)