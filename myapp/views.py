from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, world!")

def hola(request):
    return HttpResponse("¡Hola, mundo!")