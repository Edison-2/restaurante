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
        return fila.format(self.region_ed,
        self.nombre_ed, self.capital_ed )
