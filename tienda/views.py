from django.shortcuts import render, redirect
# Importamos TODOS los modelos que usaremos en este archivo
from .models import Producto, Cliente, Venta 
# Importamos TODOS los formularios que usaremos
from .forms import ProductoForm, ClienteForm, VentaForm 

# --- VISTAS DE NAVEGACIÓN Y PRODUCTOS (Las que ya tenías) ---

def catalogo(request):
    # Si el usuario está logueado mostramos productos,
    # si no, devolvemos un queryset vacío para que no se vea nada.
    if request.user.is_authenticated:
        productos = Producto.objects.all()
    else:
        productos = Producto.objects.none()
    return render(request, "catalogo.html", {"productos": productos})

def home(request):
    # Ya no redirige. Simplemente renderiza la plantilla home.html.
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html")

def pages_list(request):
    return render(request, "pages/pages_list.html")

# --- VISTAS DE CLIENTES Y VENTAS (Las nuevas) ---

# Formulario de Cliente
def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige a la lista de clientes después de guardar
            return redirect('lista_clientes') 
    else:
        form = ClienteForm()
    return render(request, 'agregar_cliente.html', {'form': form})
    
# Listado de Clientes
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

# Formulario de Venta
def agregar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
    else:
        form = VentaForm()
    return render(request, 'agregar_venta.html', {'form': form})
    
# Listado de Ventas
def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'lista_ventas.html', {'ventas': ventas})