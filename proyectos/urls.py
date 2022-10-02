from django.urls import re_path
from .views import *

urlpatterns = [
	re_path(r'^$', ProyectoListView.as_view(), name='proyecto_list'),
	re_path(r'^create/$', ProyectoCreateView),
	re_path(r'^update/(?P<slug>[\w\-]+)/$', ProyectoUpdateView),
	re_path(r'^(?P<pk>[0-9]+)/$', ProyectoDetailView.as_view()),
    re_path(r'^home/$', HomeTemplateView.as_view()),
    re_path(r'^test/$', TestView.as_view()),
    re_path(r'^buscar/$', buscar_view),
    #url(r'^obtener/(?P<articulo_id>\d+)/$', 'blog.views.articulo'),
]