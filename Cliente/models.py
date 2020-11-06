from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

class Seccion_Cliente(models.Model):
    seccion=models.CharField(max_length=30, null=True, blank=True)
    icono=models.FileField(upload_to='media' , null=True, blank=True)
    wallpaper_seccion=models.FileField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return '%s '% (self.seccion)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.icono)

    class Meta:
        verbose_name_plural = "1. Clientes "


talla_chosse=(
    ('','') ,('S','S'),('M','M'),('L','L'),('XL','XL'),('30','30'),('31','31'),('32','32'),('33','33'),('34','34'),('35','35'),('36','36'),('37','37'),('38','38'),('39','39'),('40','40'),('41','41'),('42','42'),('43','43')
)


class Coleccion(models.Model):
    nuevo=models.BooleanField(default=False)
    seccion=models.ForeignKey(Seccion_Cliente, on_delete=models.CASCADE )
    tema=models.CharField(max_length=30, null=True, blank=True)
    imagen=models.FileField(upload_to='media', null=True, blank=True, help_text='100x100')
    portada=models.FileField(upload_to='media', null=True, blank=True, help_text='100x100')
    icono=models.FileField(upload_to='media', null=True,blank=True, help_text='100x100')

    def __str__(self):
        return '%s %s'% (self.seccion,self.tema)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.imagen)

    class Meta:
        verbose_name_plural = "2. Coleccion "

class Imag_prenda_articulo(models.Model):
    tipo = models.CharField(max_length=30, null=True, blank=True)
    imagen = models.ImageField(upload_to='media', null=True, blank=True, help_text='100x100')

    def __str__(self):
        return '%s ' % (self.tipo)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.imagen)

    class Meta:
        verbose_name_plural = "3. Imag_prenda_articulo "

class Articulo(models.Model):
    seccion = models.ForeignKey(Seccion_Cliente, on_delete=models.CASCADE, null=True, blank=True)
    tipo=models.ForeignKey(Imag_prenda_articulo, on_delete=models.CASCADE, null=True, blank=True)




    def __str__(self):
        return '%s %s' % ( self.seccion,  self.tipo)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.tipo.imagen)



    class Meta:
        verbose_name_plural = "4. Articulo "



class Prenda(models.Model):
    principal_visible = models.BooleanField(default=False)
    articulo= models.ForeignKey(Articulo, on_delete=models.CASCADE, null=True, blank=True)
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE, null=True, blank=True)
    tipo=models.ForeignKey(Imag_prenda_articulo, on_delete=models.CASCADE, null=True, blank=True)




    def __str__(self):
        return '%s %s' % ( self.coleccion,  self.tipo)
        # return '%s' % (self.coleccion)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.tipo.imagen)



    class Meta:
        verbose_name_plural = "5. Prenda "

