from django.urls import path, include
from . import views

urlpatterns = [
			path('home', views.home, name="Home"),
            path('',views.home, name="Home"),
            path('catalogo-autor', views.catalogoAutor, name="catalogoAutor"),
            path('catalogo-libro', views.catalogoLibro, name= "catalogoLibro"),
            path('categoria', views.categoria, name="categoria")
		]