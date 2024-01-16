from django.urls import path
from . import views

urlpatterns=[
    path('',views.listadoProvincias),
    path('guardarProvincia/',views.guardarProvincia),
    path('eliminarProvincia/<id_ed>' ,views.eliminarProvincia),
    path('editarProvincia/<id_ed>' ,views.editarProvincia),
    path('procesarActualizacionProvincia/', views.procesarActualizacionProvincia),
    path('listadoClientes/',views.listadoClientes),
    path('eliminarCliente/<id_ed>' ,views.eliminarCliente),
    path('listadoClientes/guardarCliente/',views.guardarCliente),
    path('editarCliente/<id_ed>' ,views.editarCliente),
    path('procesarActualizacionCliente/', views.procesarActualizacionCliente),


]
