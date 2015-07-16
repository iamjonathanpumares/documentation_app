from django.contrib import admin
from .models import Modulo, TipoPaquete, Paquete

class PaqueteAdmin(admin.ModelAdmin):
	filter_horizontal = ('paquetes_requeridos',)

admin.site.register(Modulo)
admin.site.register(TipoPaquete)
admin.site.register(Paquete, PaqueteAdmin)