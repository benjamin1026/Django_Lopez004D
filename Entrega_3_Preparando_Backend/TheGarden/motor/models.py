from pyexpat import model
from django.db import models

# Create your models here.
class Cliente(models.Model):
    idCliente = models.IntegerField(primary_key=True, verbose_name='Id del Cliente')
    nombreCliente = models.CharField(max_length=20, verbose_name='NombreC')
    correoCliente = models.EmailField(verbose_name='Correo del Cliente')
    telefCliente = models.IntegerField( verbose_name='Numero del Cliente')
    direcCliente = models.CharField(max_length=30, verbose_name='Direccion del Cliente')

    def __str__(self):
        return self.nombreCliente

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id del Producto')
    nomProducto = models.CharField(max_length=30, verbose_name='NombreP')
    precioProducto = models.IntegerField(verbose_name='Precio')
    Descripcion=models.CharField(max_length=100, verbose_name='Descripcion')

    def __str__(self):
        return self.nomProducto