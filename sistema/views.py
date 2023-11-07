from django.shortcuts import render
from django.http import HttpResponse 

def saludar(request):   
    saludo="hola querido usuario"
    respuesta_http= HttpResponse(saludo)
    return respuesta_http