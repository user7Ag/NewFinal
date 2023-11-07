from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    sueldoBase = models.CharField(max_length=64)
    telefono = models.CharField(max_length=64)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True, blank=True)

class Reservas(models.Model):
    numeroDeReserva = models.CharField(max_length=64)
    nombre_cliente = models.CharField(max_length=64)
    numero_comensales = models.CharField(max_length=64)

class Inventario(models.Model):
    cantidad_platosFinalDia = models.CharField(max_length=64)
    cantidad_vasosFinalDia = models.CharField(max_length=64)
    cantidad_cuchillosFinalDia = models.CharField(max_length=64)
    cantidad_tenedoresFinalDia = models.CharField(max_length=64)

class Menu(models.Model):
    nombreDelPlato = models.CharField(max_length=64)
    precioDelPlato = models.CharField(max_length=64)
    descripcionDelPlato = models.CharField(max_length=64)

class Suministros(models.Model):
    nombreIngrediente = models.CharField(max_length=64)
    nombreBebidas = models.CharField(max_length=64)
    cantidad_Bebidas = models.CharField(max_length=64)
