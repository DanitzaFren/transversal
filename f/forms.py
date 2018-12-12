from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from f.models import Venta
from django import forms


class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
			]
		labels = {
				
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',			
		}


class VentaForm(forms.ModelForm):

	class Meta:
		model = Venta
		fields = [
			'vendedor', 
			'producto', 
			'fecha', 
			'cantidad', 
			'tienda', 
			'comentario', 
			]
		labels = {
					
			'vendedor': 'Vendedor', 
			'producto': 'Producto', 
			'fecha' : 'Fecha', 
			'cantidad': 'Cantidad', 
			'tienda' : 'Tienda', 
			'comentario' : 'Agregar comentario',		
		}