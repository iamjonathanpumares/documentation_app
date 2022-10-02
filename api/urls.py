from django.urls import re_path
from . import views

urlpatterns = [
	#url(r'^$', ProyectoListView.as_view()),
	re_path(r'^proyectos/$', views.ProyectoListAPIView.as_view()),
	re_path(r'^modulos-principales/(?P<slug>[\w\-]+)/$', views.ModulosPrincipalesListAPIView.as_view()),
	re_path(r'^tipos-paquetes/(?P<slug>[\w\-]+)/$', views.TipoPaqueteListAPIView.as_view()),
	re_path(r'^submodulos-totales/(?P<pk>[0-9]+)/$', views.SubmodulosTotalesDetailAPIView.as_view()),
	re_path(r'^paquetes/modulo/(?P<pk>[0-9]+)/$', views.ModuloDetailAPIView.as_view()),
	re_path(r'^paquetes-independientes/(?P<slug>[\w\-]+)/(?P<clave_paquete>[\w\-]+)/$', views.PaqueteListAPIView.as_view()),
	re_path(r'^paquetes-requeridos/(?P<pk>[0-9]+)/$', views.PaqueteRequeridoCreateAPIView),
	re_path(r'^paquetes/$', views.PaqueteCreateAPIView),
	re_path(r'^paquetes/(?P<pk>[0-9]+)/$', views.PaqueteDetailAPIView.as_view()),
	re_path(r'^proyectos/(?P<pk>[0-9]+)/$', views.ProyectoDetailAPIView.as_view()),
	re_path(r'^procesos/(?P<pk>[0-9]+)/$', views.ProcesoDetailAPIView.as_view()),
	# app procesos ---------------------------------------------------------
	re_path(r'^responsables/$', views.ResponsableCreateAPIView.as_view()),
	# app casos_de_uso ---------------------------------------------------------
	re_path(r'^tareas/$', views.TareaCreateAPIView.as_view()),
	re_path(r'^tareas/(?P<pk>[0-9]+)/$', views.TareaDetailAPIView.as_view()),
	re_path(r'^actores/(?P<pk>[0-9]+)/$', views.ActorDetailAPIView.as_view(), name='api-actor-detail'),
	# app diccionario_de_datos ---------------------------------------------------------
	re_path(r'^campos/$', views.CampoListCreateAPIView.as_view()),
	re_path(r'^campos/(?P<pk>[0-9]+)/$', views.CampoDetailAPIView.as_view()),
	re_path(r'^tipos-datos/(?P<pk>[0-9]+)/$', views.TipoDatoDetailAPIView.as_view()),
]