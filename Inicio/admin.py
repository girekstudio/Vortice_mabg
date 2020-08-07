from django.contrib import admin

# Register your models here.
from Inicio.models import *
from Vortice_mabg.snippers import Attr

class SliderAdmin(admin.ModelAdmin):
    list_display = Attr(Slider)+["miniatura"]
    list_display_links = Attr(Slider)
admin.site.register(Slider, SliderAdmin)

class VorticeAdmin(admin.ModelAdmin):
    list_display = Attr(Vortice)+["miniatura"]
    list_display_links = Attr(Vortice)
admin.site.register(Vortice, VorticeAdmin)

class Contacto_redesAdmin(admin.ModelAdmin):
    list_display = Attr(Contacto_redes)
    list_display_links = Attr(Contacto_redes)
admin.site.register(Contacto_redes, Contacto_redesAdmin)



