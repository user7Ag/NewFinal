from django.urls import path

from Restaurante.views import (
    EmpleadoListView, EmpleadoDetailView, EmpleadoDeleteView, EmpleadoCreateView, EmpleadoUpdateView)

from Restaurante.views import(
    ReservaListView, ReservaDetailView, ReservaDeleteView, ReservaCreateView, ReservaUpdateView)

from Restaurante.views import(
    InventarioListView, InventarioDetailView, InventarioDeleteView, InventarioCreateView, ReservaUpdateView)

from Restaurante.views import(
    MenuListView, MenuDetailView, MenuDeleteView, MenuCreateView, MenuUpdateView)




#URLS EMPLEADOS APP Restaurante

urlpatterns=[
    path("empleado/", EmpleadoListView.as_view(), name="lista_empleados"),
    path("empleado/<int:pk>/" ,EmpleadoDetailView.as_view(), name="ver_empelado"),
    path("crear-emplado/", EmpleadoCreateView.as_view(), name="crear_empleado"),
    path("editar-empleado/<int:pk>/", EmpleadoUpdateView.as_view(), name="editar_empleado"),
    path("eliminar-empleado/<int:pk>/", EmpleadoDeleteView.as_view(),name="eliminar_empleado"),
]

#URLS RESERVA APP Restaurante

urlpatterns=[
    path("reserva/", ReservaListView.as_view(), name="lista_reservas"),
    path("reserva/<int:pk>/", ReservaDetailView.as_view(), name="ver_reserva"),
    path("crear-reserva/", ReservaCreateView.as_view(), name="crear_reserva"),
    path("editar-reserva/<int:pk>/", ReservaUpdateView.as_view(), name="editar_reserva"),
    path("eliminar-reserva/<int:pk>/", ReservaDeleteView.as_view(),name="eliminar_reserva"),
]

#URLS INVENTARIO APP Restaurante

urlpatterns=[
    path("inventario/",InventarioListView.as_view(), name="lista_inventarios"),
    path("inventario/<int:pk>/", InventarioDetailView.as_view(), name="ver_inventario"),
    path("crear-inventario/", InventarioCreateView.as_view(), name="crear_inventario"),
    path("editar-inventario/<int:pk>/", InventarioUpdateView.as_view(), name="editar_inventario"),
    path("eliminar-inventario/<int:pk>/", InventarioDeleteView.as_view(), name="eliminar_inventario"),
]

#URLS Menu APP Restaurante

urlpatterns=[
    path("menu/",MenuListView.as_view(), name="lista_menus"),
    path("menu/<int:pk>/", MenuDetailView.as_view(), name="ver_menus"),
    path("crear-menu/", MenuCreateView.as_view(), name="crear_menus"),
    path("editar-menu/<int:pk>/", MenuUpdateView.as_view(), name="editar_menus"),
    path("eliminar-menu/<int:pk>/", MenuDeleteView.as_view(), name="eliminar_menus"),
]

#URLS SUMINISTROS APP Restaurante


urlpatterns=[
    path("suministro/",SuministrosListView.as_view(), name="lista_suministros"),
    path("suministro/<int:pk>/", SuministrosDetailView.as_view(), name="ver_suministros"),
    path("crear-suministro/", SuministrosCreateView.as_view(), name="crear_suministros"),
    path("editar-suministro/<int:pk>/", SuministrosUpdateView.as_view(), name="editar_suministros"),
    path("eliminar-suministro/<int:pk>/", SuministrosDeleteView.as_view(), name="eliminar_suministros"),
]


