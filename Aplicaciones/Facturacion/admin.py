from django.contrib import admin
from .models import Provincia
from .models import Cliente
from .models import Tipo
from .models import Pedido
# Register your models here.
admin.site.register(Provincia)
admin.site.register(Cliente)
admin.site.register(Tipo)
admin.site.register(Pedido)
