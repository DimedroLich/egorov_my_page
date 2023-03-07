from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from math import pi


# Create your views here.
def rect(request, width, height):
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width * height}')


def square(request, width: int):
    return HttpResponse(f'<h2>Площадь квадрата размером {width}x{width} равна {width ** 2}')


def circle(request, radius: int):
    return HttpResponse(f'<h2>Площадь круга радиусом {radius} равна {round(pi * radius ** 2, 2)}')


def get_rectangle_area(request, width, height):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')

def get_square_area(request, width: int):
    return HttpResponseRedirect(f'/calculate_geometry/square/{width}')

def get_circle_area(request, radius: int):
    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}')