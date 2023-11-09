from django.urls import path

from Restaurante.views import (
    EmpleadoListView, EmpleadoDetailView, EmpleadoCreateView, EmpleadoUpdateView, EmpleadoDeleteView,
    ReservasListView, ReservasDetailView, ReservasCreateView, ReservasUpdateView, ReservasDeleteView,
    InventarioListView, InventarioDetailView, InventarioCreateView, InventarioUpdateView, InventarioDeleteView,
    MenuListView, MenuDetailView, MenuCreateView, MenuUpdateView, MenuDeleteView,
    SuministrosListView, SuministrosDetailView, SuministrosCreateView, SuministrosUpdateView, SuministrosDeleteView
)

urlpatterns = [
    path("empleado/", EmpleadoListView.as_view(), name="lista_empleados"),
    path("empleado/<int:pk>/", EmpleadoDetailView.as_view(), name="ver_empelados"),
    path("crear-emplado/", EmpleadoCreateView.as_view(), name="crear_empleados"),
    path("editar-empleado/<int:pk>/", EmpleadoUpdateView.as_view(), name="editar_empleados"),
    path("eliminar-empleado/<int:pk>/", EmpleadoDeleteView.as_view(), name="eliminar_empleados"),

    path("reserva/", ReservasListView.as_view(), name="lista_reservas"),
    path("reserva/<int:pk>/", ReservasDetailView.as_view(), name="ver_reservas"),
    path("crear-reserva/", ReservasCreateView.as_view(), name="crear_reservas"),
    path("editar-reserva/<int:pk>/", ReservasUpdateView.as_view(), name="editar_reservas"),
    path("eliminar-reserva/<int:pk>/", ReservasDeleteView.as_view(), name="eliminar_reservas"),

    path("inventario/", InventarioListView.as_view(), name="lista_inventarios"),
    path("inventario/<int:pk>/", InventarioDetailView.as_view(), name="ver_inventarios"),
    path("crear-inventario/", InventarioCreateView.as_view(), name="crear_inventarios"),
    path("editar-inventario/<int:pk>/", InventarioUpdateView.as_view(), name="editar_inventarios"),
    path("eliminar-inventario/<int:pk>/", InventarioDeleteView.as_view(), name="eliminar_inventarios"),

    path("menu/", MenuListView.as_view(), name="lista_menus"),
    path("menu/<int:pk>/", MenuDetailView.as_view(), name="ver_menus"),
    path("crear-menu/", MenuCreateView.as_view(), name="crear_menus"),
    path("editar-menu/<int:pk>/", MenuUpdateView.as_view(), name="editar_menus"),
    path("eliminar-menu/<int:pk>/", MenuDeleteView.as_view(), name="eliminar_menus"),

    path("suministro/", SuministrosListView.as_view(), name="lista_suministros"),
    path("suministro/<int:pk>/", SuministrosDetailView.as_view(), name="ver_suministros"),
    path("crear-suministro/", SuministrosCreateView.as_view(), name="crear_suministros"),
    path("editar-suministro/<int:pk>/", SuministrosUpdateView.as_view(), name="editar_suministros"),
    path("eliminar-suministro/<int:pk>/", SuministrosDeleteView.as_view(), name="eliminar_suministros"),
]
