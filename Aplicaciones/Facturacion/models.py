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
