from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.

def home(request):
    Navbars = NavBar.objects.all()
    context = {
        "Navbars": Navbars
    } 
    return render (request, 'catalogo/home.html', context)

def catalogoAutor(request):
    Navbars = NavBar.objects.all()
    Autores = Autor.objects.all()
    context = {
        "Navbars": Navbars,
        "Autores": Autores
        
    }  
    return render (request, 'catalogo/catalogoAutor.html', context)

def catalogoLibro(request):
    Navbars = NavBar.objects.all()
    Libros = Libro.objects.all()
    context = {
        "Navbars": Navbars,
        "Libros": Libros
    }  
    return render (request, 'catalogo/catalogoLibro.html', context)

def categoria(request):
    Navbars = NavBar.objects.all()
    Categorias = Categoria.objects.all()
    Libros = Libro.objects.all().select_related('id_autor','id_categoria')
    context = {
        "Navbars": Navbars,
        "Categorias": Categorias,
        "Libros": Libros
    } 
    return render (request, 'catalogo/categoria.html', context)

def masInfo(request):
    Navbars = NavBar.objects.all()
    id_libro = request.GET.get('id_libro')
    Libros = Libro.objects.get(id_libro=id_libro)
    Autor = Libros.id_autor
    Categoria = Libros.id_categoria
    context = {
        "Navbars": Navbars,
        "Libros": Libros,
        "Autor": Autor,
        "Categoria": Categoria
    } 
    return render (request, 'catalogo/masInfo.html', context)

def buscar_categoria(request):
    libros = Libro.objects.all()
    categoria_nombre = request.GET.get('categoria', '')
    if categoria_nombre:
        libros = libros.filter(id_categoria__nombre=categoria_nombre)
    libros_data = [{
        'urlImg': libro.urlImg,
        'titulo': libro.titulo,
        'nombre_autor': libro.id_autor.nombre,
        'descripcion': libro.descripcion,
    } for libro in libros]

    return JsonResponse({'libros': libros_data})


