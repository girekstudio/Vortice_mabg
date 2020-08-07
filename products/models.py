from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

from Cliente.models import *


class Product(models.Model):
    orden = models.IntegerField(default=0)
    offer = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    stock = models.BooleanField(default=True)
    prenda=models.ForeignKey(Prenda, on_delete=models.CASCADE, null=True, blank=True )
    titulo=models.CharField(max_length=50, null=True, blank=True)
    imagen=models.ImageField(upload_to='media', null=True, blank=True, help_text='100x100')
    imagen_2=models.ImageField(upload_to='media', null=True, blank=True, help_text='100x100')
    imagen_3 = models.ImageField(upload_to='media', null=True, blank=True, help_text='100x100')
    imagen_4 = models.ImageField(upload_to='media', null=True, blank=True, help_text='100x100')
    talla=models.CharField(max_length=50, null=True, blank=True)
    precio=models.DecimalField(max_digits=999, decimal_places=2)
    precio_oferta=models.DecimalField(max_digits=999, decimal_places=2, null=True, blank=True)
    descripcion=models.CharField(max_length=500, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return '%s' % (self.titulo)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.imagen)



    class Meta:
        verbose_name_plural = "1. Producto "