from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView,ListView
from django.urls import reverse_lazy
from django.contrib import messages
from f.models import Venta
from f.forms import RegistroForm, VentaForm
# Create your views here.

class RegistroUsuario(CreateView):
	model = User
	template_name = "f/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('login')
    

def menu(request):
    return render(request, 'f/menu.html', {})

class ListaVenta(ListView):
	model = Venta
	template_name = 'f/listar.html'


class RegistroVenta(CreateView):
	model = Venta
	template_name = "f/vender.html"
	form_class = VentaForm
	success_url = reverse_lazy('menu_vendedor')


def vender(request):
    return render(request, 'f/vender.html', {})