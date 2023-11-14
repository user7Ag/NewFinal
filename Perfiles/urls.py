from django.contrib import admin
from django.urls import path

from Perfiles.views import registro, login_view, CustomLogoutView


urlpatterns = [
    # URLS Usuario y sesion
    path('Registro/', registro, name="registro"),
    path('Login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
]