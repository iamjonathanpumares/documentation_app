from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	#url(r'^$', ProyectoListView.as_view()),
	url(r'^proyectos/$', views.ProyectoListAPIView.as_view()),
	url(r'^modulos-principales/(?P<slug>[\w\-]+)/$', views.ModulosPrincipalesListAPIView.as_view()),
	url(r'^tipos-paquetes/(?P<slug>[\w\-]+)/$', views.TipoPaqueteListAPIView.as_view()),
	url(r'^submodulos-totales/(?P<pk>[0-9]+)/$', views.SubmodulosTotalesDetailAPIView.as_view()),
	url(r'^paquetes/modulo/(?P<pk>[0-9]+)/$', views.ModuloDetailAPIView.as_view()),
	url(r'^paquetes-independientes/(?P<slug>[\w\-]+)/(?P<clave_paquete>[\w\-]+)/$', views.PaqueteListAPIView.as_view()),
	url(r'^paquetes-requeridos/(?P<pk>[0-9]+)/$', views.PaqueteRequeridoCreateAPIView),
	url(r'^paquetes/$', views.PaqueteCreateAPIView),
	url(r'^paquetes/(?P<pk>[0-9]+)/$', views.PaqueteDetailAPIView.as_view()),
	url(r'^proyectos/(?P<pk>[0-9]+)/$', views.ProyectoDetailAPIView.as_view()),
	url(r'^procesos/(?P<pk>[0-9]+)/$', views.ProcesoDetailAPIView.as_view()),
	# app procesos ---------------------------------------------------------
	url(r'^responsables/$', views.ResponsableCreateAPIView.as_view()),
	# app casos_de_uso ---------------------------------------------------------
	url(r'^tareas/$', views.TareaCreateAPIView.as_view()),
	url(r'^tareas/(?P<pk>[0-9]+)/$', views.TareaDetailAPIView.as_view()),
	url(r'^actores/(?P<pk>[0-9]+)/$', views.ActorDetailAPIView.as_view(), name='api-actor-detail'),
	# app diccionario_de_datos ---------------------------------------------------------
	url(r'^campos/$', views.CampoCreateAPIView.as_view()),
	url(r'^campos/(?P<pk>[0-9]+)/$', views.CampoDetailAPIView.as_view()),
)