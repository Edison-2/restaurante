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
    path('listadoPedidos/',views.listadoPedidos),
    path('eliminarPedido/<id_ed>' ,views.eliminarPedido),
    path('guardarPedido/',views.guardarPedido),
    path('editarPedido/<id_ed>' ,views.editarPedido),
    path('procesarActualizacionPedido/', views.procesarActualizacionPedido),
    path('listadoTipos/',views.listadoTipos),
    path('eliminarTipo/<id_ed>' ,views.eliminarTipo),
    path('guardarTipo/',views.guardarTipo),
    path('editarTipo/<id_ed>' ,views.editarTipo),
    path('procesarActualizacionTipo/', views.procesarActualizacionTipo),
    
]
