from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.IntegerField(default=0,blank=True)
    cod_barras = models.CharField(max_length=100)
    descripcion = models.TextField( null=True, blank=True)
    imagen = models.CharField(max_length=100, null=True, blank=True)
    # imagen = models.ImageField(upload_to='productos', null=True, blank=True)

    def __str__(self):
        return self.nombre