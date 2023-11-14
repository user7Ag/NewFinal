from django.contrib import admin
from django.urls import path

from Perfiles.views import registro, login_view


urlpatterns = [
    # URLS Usuario y sesion
    path('Registro/', registro, name="registro"),
    path('Login/', login_view, name="login"),
]