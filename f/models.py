from django.db import models

from django.utils import timezone
# Create your models here.



class Tienda(models.Model):

	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=50)
	comuna = models.CharField(max_length=50)
	telefono = models.CharField(max_length=50)
	correo = models.CharField(max_length=50)
	encargado = models.CharField(max_length=50)

class Producto(models.Model):
	tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=50)
	precio = models.CharField(max_length=50)
	tipoProducto = models.CharField(max_length=50)



class Venta(models.Model):
	vendedor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	producto = models.CharField(max_length=50)
	fecha = models.DateTimeField(default=timezone.now)
	cantidad = models.CharField(max_length=50)
	tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
	comentario = models.CharField(max_length=100)


class Oferta(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	oprecio = models.CharField(max_length=50)


