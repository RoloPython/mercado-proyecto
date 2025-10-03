from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    # Importante: Renombramos 'correo' a 'email' para que coincida con forms.py y templates
    email = models.EmailField(unique=True) 

    def __str__(self):
        return self.nombre


class Venta(models.Model): # 👈 CAMBIO AQUÍ: de Pedido a Venta
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    # Le cambiamos 'cantidad' por 'fecha' para que coincida con el formulario VentaForm
    # Si quieres la cantidad de productos, deberías crear un modelo intermedio, pero por ahora simplificamos:
    fecha = models.DateField(auto_now_add=True) # Usamos auto_now_add=True para que se ponga la fecha automáticamente al crear.

    def __str__(self):
        return f"Venta de {self.producto} a {self.cliente}"