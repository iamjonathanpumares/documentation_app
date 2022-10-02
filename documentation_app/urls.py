from django.urls import include, re_path
from django.contrib import admin
from django.views.generic import RedirectView

from documentation_app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'documentation_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    re_path(r'^$', RedirectView.as_view(url='/proyectos/')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/', include('api.urls')),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^login/$', views.signin, name='login'),
    re_path(r'^logout/$', views.signout, name='logout'),
    re_path(r'^proyectos/', include('proyectos.urls')),
    re_path(r'^procesos/', include('procesos.urls')),
    re_path(r'^documentacion/', include('documentacion.urls')),
    re_path(r'^casos-de-uso/', include('casos_de_uso.urls')),
    re_path(r'^diccionario-de-datos/', include('diccionario_de_datos.urls')),
]
