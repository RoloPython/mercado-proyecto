from django.contrib import admin
from django.urls import path, include
from tienda import views as tienda_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", tienda_views.home, name="home"),
    path("about/", tienda_views.about, name="about"),
    path("catalogo/", tienda_views.catalogo, name="catalogo"),
    path("pages/", tienda_views.pages_list, name="pages_list"),
    path("accounts/", include("accounts.urls")),  # incluimos las urls de la app accounts
]
