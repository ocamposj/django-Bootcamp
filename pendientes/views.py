from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from pendientes.models import Tarea # Importamos la clase Tarea

# Create your views here.

def index(request):
    saludo = "Hola, Mundo! Esta es la raiz /"
    return HttpResponse(saludo) #retornamos el saludo

def tarea(request):
    return HttpResponse("Hello there")

def respuestas(request):
    lista = Tarea.objects.all() # Consultamos la database y guardamos todos
                                # los registros de la tabla Tarea
                                # como objetos y guardamos en lista
    persona = {
        "nombre":"José",
        "edad":22,
        "hobbies":["nada","nada otra vez", "nada de nada"],
        "lista_tareas":lista
    
    }
    return render(request,'inicio.html', persona)

def quinielas(request):
    resultados = {
        "primero":randint(100,999),
        "segundo":randint(100,999),
        "tercero":randint(100,999),
    }
    return render(request,'quiniela.html', resultados)