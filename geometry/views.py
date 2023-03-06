from django.shortcuts import render,HttpResponse
from math import pi
# Create your views here.
def rect(request,width,height):
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width*height}')

def square(request,width:int):
    return HttpResponse(f'<h2>Площадь квадрата размером {width}x{width} равна {width**2}')

def circle(request,radius:int):
    return HttpResponse(f'<h2>Площадь круга радиусом {radius} равна {round(pi * radius ** 2,2)}')