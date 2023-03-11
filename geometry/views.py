from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from math import pi


# Create your views here.
def rect(request, width, height):
    return render(request,'geometry/rectangle.html')

def square(request, width: int):
    return render(request,'geometry/square.html')


def circle(request, radius: int):
    return render(request,'geometry/circle.html')


def get_rectangle_area(request, width, height):
    redirected_url = reverse('rectangle',args=(width,height,))
    return HttpResponseRedirect(redirected_url)

def get_square_area(request, width: int):
    redirected_url = reverse('square',args=(width,))
    return HttpResponseRedirect(redirected_url)

def get_circle_area(request, radius: int):
    redirected_url = reverse('circle', args=(radius,))
    return HttpResponseRedirect(redirected_url)