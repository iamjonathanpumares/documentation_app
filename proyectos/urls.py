from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
	url(r'^$', ProyectoListView.as_view()),
	url(r'^create/$', ProyectoCreateView),
	url(r'^update/(?P<slug>[\w\-]+)/$', ProyectoUpdateView),
	url(r'^(?P<pk>[0-9]+)/$', ProyectoDetailView.as_view()),
    url(r'^home/$', HomeTemplateView.as_view()),
    #url(r'^obtener/(?P<articulo_id>\d+)/$', 'blog.views.articulo'),
)