from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

class Slider(models.Model):
    orden=models.IntegerField()
    imagen=models.ImageField(upload_to='media', null=True, blank=True, help_text='imagenes 500*900')
    titulo=models.CharField(max_length=30, null=True,blank=True)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 200px'>"%self.imagen)


    class Meta:
        verbose_name_plural = "2. Slider"


class Vortice(models.Model):
    favicon_amarillo=models.ImageField(upload_to='favicon', help_text='imagenes 20*20')
    favicon_negro = models.ImageField(upload_to='favicon', help_text='imagenes 20*20')
    logo_horizontal = models.ImageField(upload_to='favicon',null=True, blank=True, help_text='imagenes 20*20')
    logo_amarillo = models.ImageField(upload_to='favicon', help_text='imagenes 20*20')
    logo_negro = models.ImageField(upload_to='favicon', help_text='imagenes 20*20')
    representante = models.CharField(max_length=100, null=True, blank=True)
    celular = models.CharField(max_length=11, null=True, blank=True)
    celular2 = models.CharField(max_length=100, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    nosotros=models.TextField(max_length=500, null=True, blank=True)
    imagen = models.ImageField(upload_to='vortice', null=True, blank=True, help_text='imagenes 20*20')

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.logo_horizontal)


    class Meta:
        verbose_name_plural = "1. Vortice"



class Contacto_redes(models.Model):
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    behance = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "8. Contácto Redes Sociales"