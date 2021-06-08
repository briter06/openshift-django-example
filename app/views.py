from app.models import Persona
from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.


def index (request):
    personas = list(Persona.objects.values())
    return JsonResponse (personas,safe=False)


def add_persona(request):
    try:
        nombre = request.GET['nombre']
        edad = int(request.GET['edad'])
        persona = Persona()
        persona.nombre = nombre
        persona.edad = edad
        persona.save()
        return JsonResponse({'status':1})
    except:
        return JsonResponse({'status':0})
