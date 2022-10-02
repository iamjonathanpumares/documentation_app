# -*- coding: utf-8 -*-
from django.urls import re_path
from . import views

urlpatterns = [
	re_path(r'^(?P<slug>[\w\-]+)/$', views.ModuloListView.as_view()),
	re_path(r'^paquetes/(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/$', views.PaqueteListView.as_view(), name='paquetes-modulo'),
	re_path(r'^paquetes-requeridos/add/(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/$', views.PaqueteRequeridoView, name='paquetes-requeridos-add'),
	re_path(r'^paquetes-requeridos/(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/$', views.PaqueteRequeridoListView, name='paquetes-requeridos-list'),
	re_path(r'^submodulos/(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/$', views.SubmoduloListView.as_view(), name='submodulos-list'),
	re_path(r'^submodulos/(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/add/$', views.ModuloCreateView),
	re_path(r'^(?P<slug>[\w\-]+)/add/$', views.ModuloCreateView),
	re_path(r'^(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/$', views.ModuloUpdateView),
	#url(r'^(?P<pk>[0-9]+)/$', ProyectoDetailView.as_view()),
    #url(r'^create/$', ProyectoCreateView.as_view()),
    #url(r'^home/$', HomeTemplateView.as_view()),
    
]