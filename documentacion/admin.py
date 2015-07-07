from django.contrib import admin
from .models import Modulo, TipoPaquete, Paquete

class ModuloAdmin(admin.ModelAdmin):
	filter_horizontal = ('modulos_depende',)

admin.site.register(Modulo, ModuloAdmin)
admin.site.register(TipoPaquete)
admin.site.register(Paquete)