from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def all_horoscope(request):
    return HttpResponse('<h1>Страница со всеми знаками зодиака</h1>')


def leo(request):
    return HttpResponse('Страница знака зодика Лев')


def scorpio(request):
    return HttpResponse('Страница знака зодика Скорпион')


def aries(request):
    return HttpResponse('Страница знака зодика Овен')


def taurus(request):
    return HttpResponse('Страница знака зодика Телец')


def gemini(request):
    return HttpResponse('Страница знака зодика Близнецы')


def cancer(request):
    return HttpResponse('Страница знака зодика Рак')


def virgo(request):
    return HttpResponse('Страница знака зодика Дева')


def libra(request):
    return HttpResponse('Страница знака зодика Весы')


def sagittarius(request):
    return HttpResponse('Страница знака зодика Стрелец')


def capricorn(request):
    return HttpResponse('Страница знака зодика Козерог')


def aquarius(request):
    return HttpResponse('Страница знака зодика Водолей')


def pisces(request):
    return HttpResponse('Страница знака зодика Рыбы')
