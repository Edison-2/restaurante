from django.shortcuts import render, redirect
from .models import Provincia
from .models import Cliente

from django.contrib import messages
# Create your views here.
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
