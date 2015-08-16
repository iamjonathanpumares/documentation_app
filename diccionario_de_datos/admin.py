from django.contrib import admin

from .models import Tabla, Campo, Relacion

admin.site.register(Tabla)
admin.site.register(Campo)
admin.site.register(Relacion)
