from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    sueldoBase = models.IntegerField
    telefono = models.CharField(max_length=64)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True, blank=True)

class Reservas(models.Model):
    numeroDeReserva = models.IntegerField
    nombre_cliente = models.CharField(max_length=64)
    numero_comensales = models.IntegerField

class Inventario(models.Model):
    cantidad_platosFinalDia = models.IntegerField
    cantidad_vasosFinalDia = models.IntegerField
    cantidad_cuchillosFinalDia = models.IntegerField
    cantidad_tenedoresFinalDia = models.IntegerField

class Menu(models.Model):
    nombreDelPlato = models.CharField(max_length=64)
    precioDelPlato = models.IntegerField
    descripcionDelPlato = models.CharField(max_length=64)

class Suministros(models.Model):
    nombreIngrediente = models.CharField(max_length=64)
    nombreBebidas = models.CharField(max_length=64)
    cantidad_Bebidas = models.IntegerField
