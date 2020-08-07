from django.contrib import admin

from django.db import models

from Blogs.models import *
from Vortice_mabg.snippers import Attr


class CategoriaAdmin(admin.ModelAdmin):
    list_display = Attr(Categoria)
    list_display_links = Attr(Categoria)
admin.site.register(Categoria, CategoriaAdmin)

class BlogsAdmin(admin.ModelAdmin):
    list_display = Attr(Blogs)
    list_display_links = Attr(Blogs)
admin.site.register(Blogs, BlogsAdmin)