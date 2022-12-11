from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    cuit = models.CharField(max_length=150, verbose_name='CUIT')
    legajo = models.CharField(max_length=100, verbose_name='Legajo')
    
    
class Proveedores(models.Model):
    nombreprov = models.CharField(max_length=100, verbose_name='Nombre proveedores')
    descripcion = models.TextField(null=True, verbose_name='Descripcion')
    nombreprov = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    nombreprov = models.ManyToManyField(Clientes)   
