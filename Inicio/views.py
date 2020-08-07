from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render

# Create your views here.
from Blogs.models import Visitas_Blog, Blogs, Categoria
from Inicio.models import *
from products.models import *


def index(request):
    contexto ={
        'vortice':Vortice.objects.all().first(),
        'slider':Slider.objects.all(),
        'coleccion':Coleccion.objects.all(),
        'prenda':Prenda.objects.all(),
        'seccion': Seccion_Cliente.objects.all(),
        'products': Product.objects.all(),
        'blogs': Blogs.objects.all(),
        'categorias': Categoria.objects.all(),
        'redes': Contacto_redes.objects.all().first(),
    }
    return render(request,'index.html', contexto)


def seccion_filtro(request,secc):

    contexto ={
        'prendas': Prenda.objects.filter(coleccion__seccion__seccion=secc),
        'vortice':Vortice.objects.all().first(),
        'seccion': Seccion_Cliente.objects.all(),
        'sec': Seccion_Cliente.objects.get(seccion=secc),
        'coleccioness':Coleccion.objects.filter(seccion__seccion=secc),
        'products': Product.objects.filter(prenda__coleccion__seccion__seccion=secc),
        'blogs': Blogs.objects.all(),
        'categorias': Categoria.objects.all(),
        'redes': Contacto_redes.objects.all().first(),

    }
    return render(request,'categories.html', contexto)


def tipo_filtro(request,seccion,tipo):
    contexto ={
        'prenda': Prenda.objects.all(),
        'seccion': Seccion_Cliente.objects.all(),
        'vortice':Vortice.objects.all().first(),
        'prendas': Prenda.objects.filter(coleccion__seccion__seccion=seccion),
        'colecciones': Coleccion.objects.filter(seccion__seccion=seccion),
        'redes': Contacto_redes.objects.all().first(),
        'products': Product.objects.filter(prenda__coleccion__seccion__seccion=seccion ,prenda__tipo=tipo  ),
        'blogs': Blogs.objects.all(),
        'categorias': Categoria.objects.all(),

    }
    return render(request, 'categories.html', contexto)



def coleccion_filtro(request,seccion,coleccion):
    contexto ={
        'prenda': Prenda.objects.all(),
        'seccion': Seccion_Cliente.objects.all(),
        'vortice':Vortice.objects.all().first(),
        'prendas': Prenda.objects.filter(coleccion__seccion__seccion=seccion),
        'colecciones': Coleccion.objects.filter(seccion__seccion=seccion),
        'colec': Coleccion.objects.filter(tema=coleccion).first(),
        'redes': Contacto_redes.objects.all(),
        'products': Product.objects.filter(prenda__coleccion__tema=coleccion ),
        'blogs': Blogs.objects.all(),
        'categorias': Categoria.objects.all(),

    }
    return render(request, 'coleccion.html', contexto)




def producto_detalle(request,id):
    contexto = {
        'vortice': Vortice.objects.all().first(),
        'coleccion': Coleccion.objects.all(),
        'prenda': Prenda.objects.all(),
        'seccion': Seccion_Cliente.objects.all(),
        'products': Product.objects.get(id=id),
        'redes': Contacto_redes.objects.all(),
        'blogs': Blogs.objects.all(),
        'categorias': Categoria.objects.all(),
    }
    return render(request,'product-details.html', contexto)

def blog(request):
    contexto = {
        'visitas': Visitas_Blog.objects.all(),
        'blogs': Blogs.objects.all(),
        'categorias': Categoria.objects.all(),
        'vortice': Vortice.objects.all().first(),
        'coleccion': Coleccion.objects.all(),
        'prenda': Prenda.objects.all(),
        'seccion': Seccion_Cliente.objects.all(),
        'redes': Contacto_redes.objects.all().first(),




    }
    return render(request, "blog.html", contexto)


def post(request, n):
    try:
        Visitas_Blog(blog_id=n).save()
    except:
        visita = Visitas_Blog.objects.get(blog_id=n)
        visita.save()
    contexto = {
        'blogg': Blogs.objects.get(id=n),
        'blogs': Blogs.objects.all(),
        'categorias': Categoria.objects.all(),
        'vortice': Vortice.objects.all().first(),
        'coleccion': Coleccion.objects.all(),
        'prenda': Prenda.objects.all(),
        'seccion': Seccion_Cliente.objects.all(),
        'redes': Contacto_redes.objects.all().first(),


    }
    return render(request, "blog-single.html", contexto)

def contacto(request):
    contexto = {
        'vortice': Vortice.objects.all().first(),
    }
    if request.POST:
        enviar_email(request,request.POST['subject'],request.POST['email'],"vortice.ec@gmail.com",request.POST['message'],request.POST['name'])
    return render(request,'contact.html',contexto)



def enviar_email(request,asunto,from_email,to,mensaje,nombre):
    asunto = asunto
    from_email = from_email
    to = to
    text_content = 'Este mnsaje es importante.'
    html_content = '<p>This is an <strong>important</strong> message.</p>' \
                   '<img src="http://vortice.ec/static/imagenes/vortice.png"><br>' + mensaje
    msg = EmailMultiAlternatives(asunto, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    # print from_email
