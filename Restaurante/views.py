from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse, reverse_lazy
from Restaurante.models import Empleado, Reservas, Menu, Inventario, Suministros

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


class ReservasListView(ListView):
    model = Reservas
    template_name = 'Restaurante/lista_reservas.html'


class ReservasCreateView(CreateView):
    model = Reservas
    fields = ('numeroDeReserva', 'nombre_cliente', 'numero_comensales')
    success_url = reverse_lazy('lista_reservas')


class ReservasDetailView(DetailView):
    model = Reservas
    success_url = reverse_lazy('lista_reservas')


class ReservasUpdateView(UpdateView):
    model = Reservas
    fields = ('numeroDeReserva', 'nombre_cliente', 'numero_comensales')
    success_url = reverse_lazy('lista_reservas')

class ReservasDeleteView(DeleteView):
    model = Reservas
    success_url = reverse_lazy('lista_reservas')


# Vistas de inventario (basadas en clases)


class InventarioListView(ListView):
    model = Inventario
    template_name = 'Restaurante/lista_inventarios.html'


class InventarioCreateView(CreateView):
    model = Inventario
    fields = ('cantidad_platosFinalDia', 'antidad_vasosFinalDia', 'cantidad_cuchillosFinalDia', 'cantidad_tenedoresFinalDia')
    success_url = reverse_lazy('lista_inventarios')

class InventarioDetailView(DetailView):
    model = Inventario
    success_url = reverse_lazy('lista_inventarios')


class InventarioUpdateView(UpdateView):
    model = Inventario
    fields = ('cantidad_platosFinalDia', 'antidad_vasosFinalDia', 'cantidad_cuchillosFinalDia', 'cantidad_tenedoresFinalDia')
    success_url = reverse_lazy('lista_inventarios')


class InventarioDeleteView(DeleteView):
    model = Inventario
    success_url = reverse_lazy('lista_inventarios')


# Vistas de Menus (basadas en clases)



class MenuListView(ListView):
    model = Menu
    template_name = 'Restaurante/lista_menus.html'


class MenuCreateView(CreateView):
    model = Menu
    fields = ('nombreDelPlato', 'precioDelPlato', 'descripcionDelPlato')
    success_url = reverse_lazy('lista_menus')

class MenuDetailView(DetailView):
    model = Menu
    success_url = reverse_lazy('lista_menus')


class MenuUpdateView(UpdateView):
    model = Menu
    fields = ('nombreDelPlato', 'precioDelPlato', 'descripcionDelPlato')
    success_url = reverse_lazy('lista_menus')


class MenuDeleteView(DeleteView):
    model = Menu
    success_url = reverse_lazy('lista_menus')


# Vistas de Suministro (basadas en clases)


class SuministrosListView(ListView):
    model = Suministros
    template_name = 'Restaurante/lista_suministros.html'


class SuministrosCreateView(CreateView):
    model = Suministros
    fields = ('nombreIngrediente', 'cantidad_ingredienteXbolsa', 'nombreBebidas', 'cantidad_Bebidas')
    success_url = reverse_lazy('lista_suministros')

class SuministrosDetailView(DetailView):
    model = Suministros
    success_url = reverse_lazy('lista_suministros')


class SuministrosUpdateView(UpdateView):
    model = Suministros
    fields = ('nombreIngrediente', 'cantidad_ingredienteXbolsa', 'nombreBebidas', 'cantidad_Bebidas')
    success_url = reverse_lazy('lista_suministros')


class SuministrosDeleteView(DeleteView):
    model = Suministros
    success_url = reverse_lazy('lista_suministros')

