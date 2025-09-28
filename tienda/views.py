from django.shortcuts import render, redirect
from .models import Producto

def catalogo(request):
    # Si el usuario está logueado mostramos productos,
    # si no, devolvemos un queryset vacío para que no se vea nada.
    if request.user.is_authenticated:
        productos = Producto.objects.all()
    else:
        productos = Producto.objects.none()
    return render(request, "catalogo.html", {"productos": productos})

def home(request):
    # redirige a la vista del catálogo
    return redirect("catalogo")

def about(request):
    return render(request, "about.html")

def pages_list(request):
    return render(request, "pages/pages_list.html")
