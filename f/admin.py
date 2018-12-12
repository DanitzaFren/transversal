from django.contrib import admin

from f.models import Producto, Venta
from f.models import Tienda
from f.models import Oferta
# Register your models here.

admin.site.register(Producto)
admin.site.register(Tienda)
admin.site.register(Oferta)
admin.site.register(Venta)