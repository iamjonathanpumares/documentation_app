from django.urls import re_path
from . import views

urlpatterns = [
	re_path(r'^$', views.ActividadAPIView),
	re_path(r'^(?P<slug>[\w\-]+)/$', views.ProcesoListView.as_view()),
	re_path(r'^(?P<slug>[\w\-]+)/add/$', views.ProcesoCreateView),
	re_path(r'^actividades/(?P<id>[0-9]+)/$', views.ProcesoDetailView, name='proceso-detail'),
	re_path(r'^(?P<slug>[\w\-]+)/(?P<id>[0-9]+)/$', views.ProcesoUpdateView),
]