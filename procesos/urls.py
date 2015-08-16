from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^$', views.ActividadAPIView),
	url(r'^(?P<slug>[\w\-]+)/$', views.ProcesoListView.as_view()),
	url(r'^(?P<slug>[\w\-]+)/add/$', views.ProcesoCreateView),
	url(r'^actividades/(?P<id>[0-9]+)/$', views.ProcesoDetailView, name='proceso-detail'),
	url(r'^(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/$', views.ProcesoUpdateView),
)