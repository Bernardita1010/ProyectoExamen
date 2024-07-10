from django.shortcuts import render
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
    context = {
        "Navbars": Navbars
    } 
    return render (request, 'catalogo/categoria.html', context)

def verMas(request):
    Navbars = NavBar.objects.all()
    Libros = Libro.objects.all()
    context = {
        "Navbars": Navbars,
        "Libros": Libros
    } 
    return render (request, 'catalogo/verMas.html', context)

