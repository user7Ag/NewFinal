from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DeleteView, DetailView
from django.urls import reverse, reverse_lazy
from Restaurante.models import Empleado

# Now you can use the 'Empleado' model in your view

# Create your views here.
# Vistas de empleados (basadas en clases)

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'Restaurante/lista_empleados.html'


class EmpleadoCreateView(CreateView):
    model = Empleado
    fields = ('nombre', 'apellido', 'sueldoBase', 'telefono', 'dni', 'fecha_nacimiento')
    success_url = reverse_lazy('lista_empleados')


class EmpleadoDetailView(DetailView):
    model = Empleado
    success_url = reverse_lazy('lista_empleados')


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    fields = ('nombre', 'apellido', 'sueldoBase', 'telefono', 'dni', 'fecha_nacimiento')
    success_url = reverse_lazy('lista_empleados')


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    success_url = reverse_lazy('lista_empleados')


# Vistas de reservas (basadas en clases)

class ReservaCreateView(CreateView):
    model = Reserva
    fields = ('numeroDeReserva', 'nombre_cliente', 'numero_comensales')
    success_url = reverse_lazy('lista_reservas')

class ReservaDetailView(DetailView):
    model = Reserva
    success_url = reverse_lazy('lista_reservas')


class ReservaUpdateView(UpdateView):
    model = Reserva
    fields = ('numeroDeReserva', 'nombre_cliente', 'numero_comensales')
    success_url = reverse_lazy('lista_reservas')


class EmpleadoDeleteView(DeleteView):
    model = Reserva
    success_url = reverse_lazy('lista_reservas')


# Vistas de inventario (basadas en clases)


class InventarioCreateView(CreateView):
    model = Inventario
    fields = ('cantidad_platosFinalDia', 'antidad_vasosFinalDia', 'cantidad_cuchillosFinalDia', 'cantidad_tenedoresFinalDia')
    success_url = reverse_lazy('lista_inventarios')

class InventarioDetailView(DetailView):
    model = Reserva
    success_url = reverse_lazy('lista_inventarios')


class InventarioUpdateView(UpdateView):
    model = Reserva
    fields = ('cantidad_platosFinalDia', 'antidad_vasosFinalDia', 'cantidad_cuchillosFinalDia', 'cantidad_tenedoresFinalDia')
    success_url = reverse_lazy('lista_inventarios')


class InventarioDeleteView(DeleteView):
    model = Reserva
    success_url = reverse_lazy('lista_inventarios')


# Vistas de Menus (basadas en clases)

class MenuCreateView(CreateView):
    model = Menu
    fields = ('nombreDelPlato', 'precioDelPlato', 'descripcionDelPlato')
    success_url = reverse_lazy('lista_menus')

class MenuDetailView(DetailView):
    model = Menus
    success_url = reverse_lazy('lista_menus')


class MenuUpdateView(UpdateView):
    model = Menu
    fields = ('nombreDelPlato', 'precioDelPlato', 'descripcionDelPlato')
    success_url = reverse_lazy('lista_menus')


class MenuDeleteView(DeleteView):
    model = Menu
    success_url = reverse_lazy('lista_menus')


# Vistas de Suministro (basadas en clases)

class SuministroCreateView(CreateView):
    model = Suministros
    fields = ('nombreIngrediente', 'cantidad_ingredienteXbolsa', 'nombreBebidas', 'cantidad_Bebidas')
    success_url = reverse_lazy('lista_suministros')

class SuministroDetailView(DetailView):
    model = Suministros
    success_url = reverse_lazy('lista_suministros')


class SuministroUpdateView(UpdateView):
    model = Suministros
     fields = ('nombreIngrediente', 'cantidad_ingredienteXbolsa', 'nombreBebidas', 'cantidad_Bebidas')
    success_url = reverse_lazy('lista_suministros')


class SuministroDeleteView(DeleteView):
    model = Suministros
    success_url = reverse_lazy('lista_suministros')

