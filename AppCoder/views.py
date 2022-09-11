from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse
# Create your views here.
def curso(request):

    materia = Curso(nombre="Diseño", camada = 12345)

    materia.save()

    return HTTPResponse(f"Estoy guardando el primer curso: {materia.nombre}")


def entregables(request):
    ente1 = Entregable(nombre="Examen 1",fechaEntrega="2022-9-08")

    ente1.save() #guardar en la base de datos

    return HttpResponse(f"He guardado: {ente1.nombre} con fecha {ente1.fechaEntrega} ")
