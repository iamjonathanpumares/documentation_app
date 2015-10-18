from django.contrib import admin

from .models import Tabla, Campo, TipoDato, Relacion

admin.site.register(Tabla)
admin.site.register(Campo)
admin.site.register(TipoDato)
admin.site.register(Relacion)
