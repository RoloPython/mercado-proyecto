from django.contrib import admin
from django.urls import path, include # Asegúrate de tener 'include' importado
from tienda import views as tienda_views

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # 🌟 Solución: Incluimos TODAS las rutas definidas en tienda/urls.py.
    # Como la ruta es vacía (""), se mapearán como /clientes/ y /ventas/.
    path("", include("tienda.urls")), 
    
    # Mantenemos las rutas específicas que tienes en tu proyecto principal, 
    # pero deben ir DESPUÉS de la línea 'include' si las vistas están en tienda/views.py
    # Nota: Si home, about, catalogo y pages_list son tus vistas principales, 
    # deberían estar en el archivo 'tienda/urls.py' en lugar de aquí.
    # Por ahora, las dejamos para evitar que se rompa tu navegación existente:

    path("", tienda_views.home, name="home"),
    path("about/", tienda_views.about, name="about"),
    path("catalogo/", tienda_views.catalogo, name="catalogo"),
    path("pages/", tienda_views.pages_list, name="pages_list"),
    path("accounts/", include("accounts.urls")), 
]