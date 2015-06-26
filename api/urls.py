from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	#url(r'^$', ProyectoListView.as_view()),
	url(r'^proyectos/$', views.ProyectoListAPIView.as_view()),
	url(r'^paquetes/$', views.PaqueteCreateAPIView),
	url(r'^proyectos/(?P<pk>[0-9]+)/$', views.ProyectoDetailAPIView.as_view()),
	url(r'^procesos/(?P<pk>[0-9]+)/$', views.ProcesoDetailAPIView.as_view()),
)