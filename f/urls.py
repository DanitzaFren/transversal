from django.urls import path
from . import views


urlpatterns = [
     path('registrar', views.RegistroUsuario.as_view(), name='usuario'),
   
	]