from django.contrib import admin
from .models import Producto   # 👈 importa el mismo nombre

admin.site.register(Producto)
