from django.contrib import admin

# Register your models here.
from Cliente.models import *
from Vortice_mabg.snippers import Attr


class Seccion_ClienteAdmin(admin.ModelAdmin):
    list_display = Attr(Seccion_Cliente)+["miniatura"]
    list_display_links = Attr(Seccion_Cliente)
admin.site.register(Seccion_Cliente, Seccion_ClienteAdmin)

class ColeccionAdmin(admin.ModelAdmin):
    list_display = Attr(Coleccion)+["miniatura"]
    list_display_links = Attr(Coleccion)
admin.site.register(Coleccion, ColeccionAdmin)



# class ArticuloAdmin(admin.ModelAdmin):
#     list_display = Attr(Articulo)+["miniatura"]
#     list_display_links = Attr(Articulo)
# admin.site.register(Articulo, ArticuloAdmin)
#
# class Imag_prenda_articuloAdmin(admin.ModelAdmin):
#     list_display = Attr(Imag_prenda_articulo)+["miniatura"]
#     list_display_links = Attr(Imag_prenda_articulo)
# admin.site.register(Imag_prenda_articulo, Imag_prenda_articuloAdmin)

# class PrendaAdmin(admin.ModelAdmin):
#     # list_display = Attr(Prenda)+["miniatura"]
#     list_display = Attr(Prenda)
#     list_display_links = Attr(Prenda)
# admin.site.register(Prenda, PrendaAdmin)