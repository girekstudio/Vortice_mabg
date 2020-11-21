from django.contrib import admin

# Register your models here.
from Vortice_mabg.snippers import Attr
from products.models import *



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = Attr(Product)+["miniatura"]
    list_display_links = Attr(Product)


# class Admin(admin.ModelAdmin):
#     list_display = Attr()
#     list_display_links = Attr()
# admin.site.register(, Admin)
