from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'documentation_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^proyectos/', include('proyectos.urls')),
    url(r'^procesos/', include('procesos.urls')),
    url(r'^documentacion/', include('documentacion.urls')),
    url(r'^casos-de-uso/', include('casos_de_uso.urls')),
    url(r'^diccionario-de-datos/', include('diccionario_de_datos.urls')),
)
