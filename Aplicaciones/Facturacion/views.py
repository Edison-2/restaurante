from django.shortcuts import render, redirect
from .models import Provincia
from .models import Cliente
from .models import Pedido
from .models import Tipo
from .models import Platillo
from .models import Detalle
from .models import Ingrediente
from .models import Receta



from django.contrib import messages
# Create your views here.
def index(request):
    # Tu lógica aquí
    return render(request, 'index.html')

def listadoProvincias(request):
    restauramteBdd=Provincia.objects.all()
    return render(request,"listadoProvincias.html",{'provincias':restauramteBdd})
def guardarProvincia(request):
    region_ed = request.POST["region_ed"]
    nombre_ed = request.POST["nombre_ed"]
    capital_ed = request.POST["capital_ed"]
    prefijo_ed = request.POST["prefijo_ed"]
    nuevaProvincia = Provincia.objects.create(region_ed=region_ed, nombre_ed=nombre_ed, capital_ed=capital_ed, prefijo_ed=prefijo_ed)
    messages.success(request, 'Provincia Guardada Exitosamente')
    return redirect('/')
def eliminarProvincia(request, id):
    provinciaEliminar = Provincia.objects.get(id_ed=id)
    provinciaEliminar.delete()
    messages.success(request, 'Provincia Eliminada Exitosamente')
    return redirect('/')
def editarProvincia(request, id):
    provinciaEditar = Provincia.objects.get(id_ed=id)
    return render(request, 'editarProvincia.html', {'provincia': provinciaEditar})
def procesarActualizacionProvincia(request):
    id_ed = request.POST["id_ed"]
    region_ed = request.POST["region_ed"]
    nombre_ed = request.POST["nombre_ed"]
    capital_ed = request.POST["capital_ed"]
    prefijo_ed = request.POST["prefijo_ed"]
    # Obtener la provincia a editar
    provinciaEditar = Provincia.objects.get(id_ed=id_ed)
    # Actualizar los datos de la provincia
    provinciaEditar.region_ed = region_ed
    provinciaEditar.nombre_ed = nombre_ed
    provinciaEditar.capital_ed = capital_ed
    provinciaEditar.prefijo_ed = prefijo_ed
    # Guardar los cambios
    provinciaEditar.save()
    messages.success(request, 'Provincia Actualizada Exitosamente')
    return redirect('/')

def listadoClientes(request):
    clientesBdd = Cliente.objects.all()
    provinciaBdd = Provincia.objects.all()

    return render(request, 'listadoClientes.html', {'clientes': clientesBdd, 'provincias': provinciaBdd})

def eliminarCliente(request,id_ed):
    clienteEliminar=Cliente.objects.get(id_ed=id_ed)
    clienteEliminar.delete()
    messages.success(request, 'CLIENTE ELIMINADO EXITOSAMENTE')
    return redirect('/listadoClientes/')

def guardarCliente(request):
    id_provincia=request.POST["id_provincia"]
    #capturando el tipo seleccionado por el usuario
    provinciaSeleccionado=Provincia.objects.get(id_ed=id_provincia)

    cedula_ed=request.POST["cedula_ed"]
    apellido_ed=request.POST["apellido_ed"]
    nombre_ed=request.POST["nombre_ed"]
    direccion_ed=request.POST["direccion_ed"]
    fecha_nacimiento_ed=request.POST["fecha_nacimiento_ed"]
    correo_ed=request.POST["correo_ed"]
    #Insertando datos mediante el ORM de django

    cliente =Cliente.objects.create(cedula_ed=cedula_ed,apellido_ed=apellido_ed,nombre_ed=nombre_ed,direccion_ed=direccion_ed,fecha_nacimiento_ed=fecha_nacimiento_ed,correo_ed=correo_ed, provincia_ed=provinciaSeleccionado)
    messages.success(request, 'CLIENTE GUARDADO EXITOSAMENTE')
    return redirect('/listadoClientes/')

def editarCliente(request, id_ed):
    clienteEditar=Cliente.objects.get(id_ed=id_ed)
    clientesBdd=Cliente.objects.all()
    provinciaBdd = Provincia.objects.all()
    return  render(request, 'editarCliente.html',{'cliente':clienteEditar,'clientes':clientesBdd,'provincias': provinciaBdd})


def procesarActualizacionCliente(request):
    id_ed = request.POST["id_ed"]
    id_provincia = request.POST["id_provincia"]
    provinciaSeleccionado = Provincia.objects.get(id_ed=id_provincia)
    cedula_ed = request.POST["cedula_ed"]
    apellido_ed = request.POST["apellido_ed"]
    nombre_ed = request.POST["nombre_ed"]
    direccion_ed = request.POST["direccion_ed"]
    fecha_nacimiento_ed = request.POST["fecha_nacimiento_ed"]
    correo_ed = request.POST["correo_ed"]

    # Insertando datos mediante el ORM de DJANGO
    clienteEditar = Cliente.objects.get(id_ed=id_ed)
    clienteEditar.provincia_ed = provinciaSeleccionado  # Corregido el nombre del campo
    clienteEditar.cedula_ed = cedula_ed
    clienteEditar.apellido_ed = apellido_ed  # Corregido el nombre del campo
    clienteEditar.nombre_ed = nombre_ed
    clienteEditar.direccion_ed = direccion_ed  # Corregido el nombre del campo
    clienteEditar.fecha_nacimiento_ed = fecha_nacimiento_ed
    clienteEditar.correo_ed = correo_ed  # Corregido el nombre del campo
    clienteEditar.save()

    messages.success(request, 'Cliente ACTUALIZADO Exitosamente')
    return redirect('/listadoClientes/')

def listadoPedidos(request):
    pedidosBdd = Pedido.objects.all()
    clienteBdd = Cliente.objects.all()

    return render(request, 'listadoPedidos.html', {'pedidos': pedidosBdd, 'clientes': clienteBdd})

def eliminarPedido(request,id_ed):
    pedidoEliminar=Pedido.objects.get(id_ed=id_ed)
    pedidoEliminar.delete()
    messages.success(request, 'PEDIDO ELIMINADO EXITOSAMENTE')
    return redirect('/listadoPedidos/')

def guardarPedido(request):
    id_cliente=request.POST["id_cliente"]
    #capturando el tipo seleccionado por el usuario
    clienteSeleccionado=Cliente.objects.get(id_ed=id_cliente)

    fecha_ed=request.POST["fecha_ed"]
    estado_ed=request.POST["estado_ed"]
    observaciones_ed=request.POST["observaciones_ed"]
    #Insertando datos mediante el ORM de django

    pedido =Pedido.objects.create(fecha_ed=fecha_ed,estado_ed=estado_ed,observaciones_ed=observaciones_ed,cliente_ed=clienteSeleccionado)
    messages.success(request, 'CLIENTE GUARDADO EXITOSAMENTE')
    return redirect('/listadoPedidos/')

def editarPedido(request, id_ed):
    pedidoEditar=Pedido.objects.get(id_ed=id_ed)
    pedidosBdd=Pedido.objects.all()
    clienteBdd = Cliente.objects.all()
    return  render(request, 'editarPedido.html',{'pedido':pedidoEditar,'pedidos':pedidosBdd,'clientes': clienteBdd})

def procesarActualizacionPedido(request):
    id_ed = request.POST["id_ed"]
    id_cliente = request.POST["id_cliente"]
    clienteSeleccionado = Cliente.objects.get(id_ed=id_cliente)
    fecha_ed = request.POST["fecha_ed"]
    estado_ed = request.POST["estado_ed"]
    observaciones_ed = request.POST["observaciones_ed"]
    # Insertando datos mediante el ORM de DJANGO
    pedidoEditar = Pedido.objects.get(id_ed=id_ed)
    pedidoEditar.cliente_ed = clienteSeleccionado
    pedidoEditar.fecha_ed = fecha_ed
    pedidoEditar.estado_ed = estado_ed
    pedidoEditar.observaciones_ed = observaciones_ed
    pedidoEditar.save()

    messages.success(request, 'PEDIDO ACTUALIZADO CORRECTAMENTE')
    return redirect('/listadoPedidos/')


def listadoTipos(request):
    tipoBdd = Tipo.objects.all()
    return render(request, 'listadoTipos.html', {'tipos': tipoBdd})


def guardarTipo(request):
    nombre_ed = request.POST["nombre_ed"]
    descripcion_ed = request.POST["descripcion_ed"]
    categoria_ed = request.POST.get("categoria_ed")  # Agregando la obtención de la categoría desde el formulario
    fotografia = request.FILES.get("fotografia")
    # Insertando datos mediante el ORM de Django
    tipo = Tipo.objects.create(nombre_ed=nombre_ed, descripcion_ed=descripcion_ed, categoria_ed=categoria_ed, fotografia=fotografia)
    messages.success(request, 'TIPO DE COMIDA GUARDADO EXITOSAMENTE')
    return redirect('/listadoTipos/')


def eliminarTipo(request,id_ed):
    tipoEliminar=Tipo.objects.get(id_ed=id_ed)
    tipoEliminar.delete()
    messages.success(request, 'TIPO DE COMIDA ELIMINADO EXITOSAMENTE')
    return redirect('/listadoTipos/')
def editarTipo(request, id_ed):
    tipoEditar=Tipo.objects.get(id_ed=id_ed)
    tiposBdd=Tipo.objects.all()
    return  render(request, 'editarTipo.html',{'tipo':tipoEditar,'tipos':tiposBdd})
def procesarActualizacionTipo(request):
    id_ed = request.POST["id_ed"]
    nombre_ed = request.POST["nombre_ed"]
    descripcion_ed = request.POST["descripcion_ed"]
    categoria_ed = request.POST.get("categoria_ed")  # Agregando la obtención de la categoría desde el formulario
    fotografia = request.FILES.get("fotografia")  # Usando FILES para obtener el archivo

    # Obteniendo el objeto Tipo a actualizar
    tipoEditar = Tipo.objects.get(id_ed=id_ed)

    # Actualizando los campos del objeto
    tipoEditar.nombre_ed = nombre_ed
    tipoEditar.descripcion_ed = descripcion_ed
    tipoEditar.categoria_ed = categoria_ed  # Agregando la actualización del campo de categoría
    tipoEditar.fotografia = fotografia

    # Guardando los cambios en la base de datos
    tipoEditar.save()

    messages.success(request, 'SU TIPO DE COMIDA FUE ACTUALIZADO CORRECTAMENTE')
    return redirect('/listadoTipos/')

def listadoPlatillos(request):
    platillosBdd = Platillo.objects.all()
    tipoBdd = Tipo.objects.all()
    return render(request, 'listadoPlatillos.html', {'platillos': platillosBdd, 'tipos': tipoBdd})
def guardarPlatillo(request):
    id_tipo=request.POST["id_tipo"]
    #capturando el tipo seleccionado por el usuario
    tipoSeleccionado=Tipo.objects.get(id_ed=id_tipo)
    nombre_ed=request.POST["nombre_ed"]
    precio_ed=request.POST["precio_ed"]
    disponibilidad_ed=request.POST["disponibilidad_ed"]
    fotografia=request.FILES.get("fotografia")
    #Insertando datos mediante el ORM de django
    platillo =Platillo.objects.create(nombre_ed=nombre_ed,precio_ed=precio_ed,disponibilidad_ed=disponibilidad_ed,fotografia=fotografia,tipo_ed=tipoSeleccionado)
    messages.success(request, 'CLIENTE GUARDADO EXITOSAMENTE')
    return redirect('/listadoPlatillos/')
def eliminarPlatillo(request,id_ed):
    platilloEliminar=Platillo.objects.get(id_ed=id_ed)
    platilloEliminar.delete()
    messages.success(request, 'PLATILLO ELIMINADO EXITOSAMENTE')
    return redirect('/listadoPlatillos/')
def editarPlatillo(request, id_ed):
    platilloEditar=Platillo.objects.get(id_ed=id_ed)
    platillosBdd=Tipo.objects.all()
    tipoBdd=Tipo.objects.all()
    return  render(request, 'editarPlatillo.html',{'platillo':platilloEditar,'platillos':platillosBdd, 'tipos':tipoBdd})

def procesarActualizacionPlatillo(request):
    id_ed = request.POST["id_ed"]
    id_tipo = request.POST["id_tipo"]
    tipoSeleccionado = Tipo.objects.get(id_ed=id_tipo)
    nombre_ed = request.POST["nombre_ed"]
    precio_ed = request.POST["precio_ed"]
    disponibilidad_ed = request.POST["disponibilidad_ed"]
    fotografia=request.POST["fotografia"]

    # Insertando datos mediante el ORM de DJANGO
    platilloEditar = Platillo.objects.get(id_ed=id_ed)
    platilloEditar.tipo_ed = tipoSeleccionado  # Corregido el nombre del campo
    platilloEditar.nombre_ed = nombre_ed
    platilloEditar.precio_ed = precio_ed  # Corregido el nombre del campo
    platilloEditar.disponibilidad_ed = disponibilidad_ed
    platilloEditar.fotografia=fotografia

    platilloEditar.save()

    messages.success(request, 'PLATILLO ACTUALIZADO CORRECTAMENTE')
    return redirect('/listadoPlatillos/')

def listadoDetalles(request):
    detalleplatillosBdd = Detalle.objects.all()

    pedidoBdd = Pedido.objects.all()
    platilloBdd = Platillo.objects.all()

    return render(request, 'listadoDetalles.html', {'detalles': detalleplatillosBdd, 'platillos': platilloBdd,'pedidos': pedidoBdd})

def eliminarDetalle(request,id_ed):
    detalleEliminar=Detalle.objects.get(id_ed=id_ed)
    detalleEliminar.delete()
    messages.success(request, 'DETALLE ELIMINADO EXITOSAMENTE')
    return redirect('/listadoDetalles/')

def guardarDetalle(request):
    id_platillo=request.POST["id_platillo"]
    id_pedido=request.POST["id_pedido"]
    #capturando el tipo seleccionado por el usuario
    platilloSeleccionado=Platillo.objects.get(id_ed=id_platillo)
    pedidoSeleccionado=Pedido.objects.get(id_ed=id_pedido)

    descripcion_ed=request.POST["descripcion_ed"]
    cantidad_ed=request.POST["cantidad_ed"]
    fecha_ed=request.POST["fecha_ed"]
    #Insertando datos mediante el ORM de django

    detalle =Detalle.objects.create(descripcion_ed=descripcion_ed,cantidad_ed=cantidad_ed,fecha_ed=fecha_ed,platillo_ed=platilloSeleccionado,pedido_ed=pedidoSeleccionado)
    messages.success(request, 'DETALLE DEL PLATILLO GUARDADO EXITOSAMENTE')
    return redirect('/listadoDetalles/')


def editarDetalle(request, id_ed):
    detalleEditar=Detalle.objects.get(id_ed=id_ed)
    detallesBdd=Detalle.objects.all()
    platilloBdd=Platillo.objects.all()
    pedidoBdd=Pedido.objects.all()
    return  render(request, 'editarDetalle.html',{'detalle':detalleEditar,'detalles':detallesBdd, 'platillos':platilloBdd, 'pedidos':pedidoBdd})


def procesarActualizacionDetalle(request):
    id_ed = request.POST["id_ed"]
    id_platillo = request.POST["id_platillo"]
    platilloSeleccionado = Platillo.objects.get(id_ed=id_platillo)
    id_pedido = request.POST["id_pedido"]
    pedidoSeleccionado = Pedido.objects.get(id_ed=id_pedido)
    descripcion_ed = request.POST["descripcion_ed"]
    cantidad_ed = request.POST["cantidad_ed"]
    fecha_ed = request.POST["fecha_ed"]


    # Insertando datos mediante el ORM de DJANGO
    detalleEditar = Detalle.objects.get(id_ed=id_ed)
    detalleEditar.platillo_ed = platilloSeleccionado  # Corregido el nombre del campo
    detalleEditar.pedido_ed = pedidoSeleccionado  # Corregido el nombre del campo
    detalleEditar.descripcion_ed = descripcion_ed
    detalleEditar.cantidad_ed = cantidad_ed  # Corregido el nombre del campo
    detalleEditar.fecha_ed = fecha_ed
    detalleEditar.save()

    messages.success(request, 'DETALLE PLATILLO ACTUALIZADO CORRECTAMENTE')
    return redirect('/listadoDetalles/')

def listadoIngredientes(request):
    ingredientesBdd = Ingrediente.objects.all()
    return render(request, 'listadoIngredientes.html', {'ingredientes': ingredientesBdd})

def eliminarIngrediente(request,id_ed):
    ingredienteEliminar=Ingrediente.objects.get(id_ed=id_ed)
    ingredienteEliminar.delete()
    messages.success(request, 'INGREDIENTE ELIMINADO EXITOSAMENTE')
    return redirect('/listadoIngredientes/')


def guardarIngrediente(request):
    nombre_ed = request.POST["nombre_ed"]
    descripcion_ed=request.POST["descripcion_ed"]
    unidad_medida_ed=request.POST["unidad_medida_ed"]
    fecha_caducidad_ed=request.POST["fecha_caducidad_ed"]
    fotografia=request.FILES.get("fotografia")
    #Insertando datos mediante el ORM de django
    ingrediente =Ingrediente.objects.create(nombre_ed=nombre_ed,descripcion_ed=descripcion_ed,unidad_medida_ed=unidad_medida_ed,fecha_caducidad_ed=fecha_caducidad_ed,fotografia=fotografia)
    messages.success(request, 'INGREDIENTE GUARDADO EXITOSAMENTE')
    return redirect('/listadoIngredientes')

def editarIngrediente(request, id_ed):
    ingredienteEditar=Ingrediente.objects.get(id_ed=id_ed)
    ingredientesBdd=Ingrediente.objects.all()
    return  render(request, 'editarIngrediente.html',{'ingrediente':ingredienteEditar,'ingredientes':ingredientesBdd})


def procesarActualizacionIngrediente(request):
    id_ed=request.POST["id_ed"]
    nombre_ed=request.POST["nombre_ed"]
    descripcion_ed=request.POST["descripcion_ed"]
    unidad_medida_ed=request.POST["unidad_medida_ed"]
    fecha_caducidad_ed=request.POST["fecha_caducidad_ed"]
    fotografia=request.POST["fotografia"]

    #Insertando datos mediante el ORM de DJANGO
    ingredienteEditar=Ingrediente.objects.get(id_ed=id_ed)
    ingredienteEditar.nombre_ed=nombre_ed
    ingredienteEditar.descripcion_ed=descripcion_ed
    ingredienteEditar.unidad_medida_ed=unidad_medida_ed
    ingredienteEditar.fecha_caducidad_ed=fecha_caducidad_ed
    ingredienteEditar.fotografia=fotografia
    ingredienteEditar.save()
    messages.success(request,
      'PROVINCIA ACTUALIZADA EXITOSAMENTE')
    return redirect('/listadoIngredientes/')

def listadoRecetas(request):
    recetasBdd = Receta.objects.all()

    ingredienteBdd = Ingrediente.objects.all()
    platilloBdd = Platillo.objects.all()

    return render(request, 'listadoRecetas.html', {'recetas': recetasBdd, 'ingredientes': ingredienteBdd,'platillos': platilloBdd})

def eliminarReceta(request,id_ed):
    recetaEliminar=Receta.objects.get(id_ed=id_ed)
    recetaEliminar.delete()
    messages.success(request, 'RECETA ELIMINADA EXITOSAMENTE')
    return redirect('/listadoRecetas/')


def guardarReceta(request):
    id_platillo=request.POST["id_platillo"]
    id_ingrediente=request.POST["id_ingrediente"]
    #capturando el tipo seleccionado por el usuario
    platilloSeleccionado=Platillo.objects.get(id_ed=id_platillo)
    ingredienteSeleccionado=Ingrediente.objects.get(id_ed=id_ingrediente)

    cantidad_ed=request.POST["cantidad_ed"]
    procedimiento_ed=request.POST["procedimiento_ed"]
    #Insertando datos mediante el ORM de django

    receta =Receta.objects.create(cantidad_ed=cantidad_ed,procedimiento_ed=procedimiento_ed,platillo_ed=platilloSeleccionado,ingrediente_ed=ingredienteSeleccionado)
    messages.success(request, 'RECETA DEL PLATILLO GUARDADO EXITOSAMENTE')
    return redirect('/listadoRecetas/')

def editarReceta(request, id_ed):
    recetaEditar=Receta.objects.get(id_ed=id_ed)
    recetasBdd=Receta.objects.all()
    platilloBdd=Platillo.objects.all()
    ingredienteBdd=Ingrediente.objects.all()
    return  render(request, 'editarReceta.html',{'receta':recetaEditar,'recetas':recetasBdd, 'platillos':platilloBdd, 'ingredientes':ingredienteBdd})

def procesarActualizacionReceta(request):
    id_ed = request.POST["id_ed"]
    id_platillo = request.POST["id_platillo"]
    platilloSeleccionado = Platillo.objects.get(id_ed=id_platillo)
    id_ingrediente = request.POST["id_ingrediente"]
    ingredienteSeleccionado = Ingrediente.objects.get(id_ed=id_ingrediente)


    cantidad_ed = request.POST["cantidad_ed"]
    procedimiento_ed = request.POST["procedimiento_ed"]


    # Insertando datos mediante el ORM de DJANGO
    recetaEditar = Receta.objects.get(id_ed=id_ed)
    recetaEditar.platillo_ed = platilloSeleccionado  # Corregido el nombre del campo
    recetaEditar.ingrediente_ed = ingredienteSeleccionado  # Corregido el nombre del campo
    recetaEditar.cantidad_ed = cantidad_ed
    recetaEditar.procedimiento_ed = procedimiento_ed  # Corregido el nombre del campo
    recetaEditar.save()

    messages.success(request, 'RECETA  ACTUALIZADA CORRECTAMENTE')
    return redirect('/listadoRecetas/')
