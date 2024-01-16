from django.contrib import admin

# Register your models here.
from .models import  Provincia
from .models import  Tipo
from .models import  Cliente
from .models import  Pedido
from .models import  Platillo
from .models import  Detalle
from .models import  Ingrediente
from .models import  Receta

# Register your models here.
admin.site.register(Provincia)
admin.site.register(Tipo)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Platillo)
admin.site.register(Detalle)
admin.site.register(Ingrediente)
admin.site.register(Receta)
