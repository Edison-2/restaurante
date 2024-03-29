from django.db import models

# Create your models here.

class Provincia(models.Model):
    id_ed=models.AutoField(primary_key=True)
    region_ed = models.CharField(max_length=255)
    nombre_ed = models.CharField(max_length=255)
    capital_ed = models.CharField(max_length=255)
    prefijo_ed= models.CharField(max_length=225, null=True,blank=True)


    def __str__(self):
        fila="{0};{1} {2}"
        return fila.format(self.region_ed, self.nombre_ed, self.capital_ed )

class Cliente(models.Model):
    id_ed = models.AutoField(primary_key=True)
    cedula_ed = models.CharField(max_length=10)
    apellido_ed = models.CharField(max_length=150,null=True, blank=True)
    nombre_ed = models.CharField(max_length=150)
    direccion_ed = models.CharField(max_length=150,null=True, blank=True)
    fecha_nacimiento_ed = models.DateField(null=True, blank=True)
    correo_ed = models.EmailField()
    provincia_ed = models.ForeignKey(Provincia, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        fila="{0}: {1} {2} {3} {4} {5} {6}"
        return fila.format(self.id_ed, self.cedula_ed, self.apellido_ed, self.nombre_ed, self.direccion_ed, self.fecha_nacimiento_ed,self.correo_ed)

class Pedido(models.Model):
    id_ed = models.AutoField(primary_key=True)
    fecha_ed = models.DateField()
    estado_ed = models.CharField(max_length=50)
    observaciones_ed = models.TextField()
    cliente_ed = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        fila="{0}: {1} {2} "
        return fila.format(self.id_ed, self.fecha_ed, self.estado_ed)

class Tipo(models.Model):
    id_ed = models.AutoField(primary_key=True)
    nombre_ed = models.CharField(max_length=150)
    descripcion_ed = models.TextField()
    categoria_ed=models.CharField(max_length=150, null=True,blank=True)
    fotografia=models.FileField(upload_to='tipo', null=True,blank=True)

    def __str__(self):
        fila="{0}: {1} {2} "
        return fila.format(self.id_ed, self.nombre_ed, self.descripcion_ed)

class Platillo(models.Model):
    id_ed = models.AutoField(primary_key=True)
    nombre_ed = models.CharField(max_length=100)
    precio_ed = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad_ed = models.CharField(max_length=50)
    fotografia=models.FileField(upload_to='platillo', null=True,blank=True)
    tipo_ed = models.ForeignKey(Tipo, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        fila="{0}: {1} {2} {3}"
        return fila.format(self.id_ed, self.nombre_ed, self.precio_ed, self.disponibilidad_ed)
class Detalle(models.Model):
    id_ed = models.AutoField(primary_key=True)
    descripcion_ed = models.TextField()
    cantidad_ed = models.IntegerField()
    fecha_ed = models.DateField()
    pedido_ed = models.ForeignKey(Pedido, null=True, blank=True, on_delete=models.PROTECT)
    platillo_ed = models.ForeignKey(Platillo, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        fila="{0}: {1} {2} {3}"
        return fila.format(self.id_ed, self.descripcion_ed, self.calorias_ed, self.fecha_ed)

class Ingrediente(models.Model):
    id_ed = models.AutoField(primary_key=True)
    nombre_ed = models.CharField(max_length=100)
    descripcion_ed = models.CharField(max_length=100)
    unidad_medida_ed = models.CharField(max_length=20)
    fecha_caducidad_ed = models.DateField()
    fotografia=models.FileField(upload_to='ingrediente', null=True,blank=True)


    def __str__(self):
        fila="{0}: {1} {2} {3} {4}"
        return fila.format(self.id_ed, self.nombre_ed, self.descripcion_ed, self.unidad_medida_ed, self.fecha_caducidad_ed, self.fotografia)

class Receta(models.Model):
    id_ed = models.AutoField(primary_key=True)
    cantidad_ed = models.CharField(max_length=100)
    procedimiento_ed = models.CharField(max_length=500)
    platillo_ed = models.ForeignKey(Platillo, on_delete=models.PROTECT)
    ingrediente_ed = models.ForeignKey(Ingrediente, null=True, blank=True, on_delete=models.PROTECT)


    def __str__(self):
        fila="{0}: {1} {2} "
        return fila.format(self.id_ed, self.cantidad_ed, self.procedimiento_ed)
