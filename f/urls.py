from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns = [
     path('registrar', views.RegistroUsuario.as_view(), name='usuario'),
     path('listar',views.ListaVenta.as_view(), name='listar'),
     path('', views.menu, name="menu_vendedor"),  
   	 path('venta', views.vender, name="venta_vendedor"), 
    
	]