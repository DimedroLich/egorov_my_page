from django.shortcuts import render
from dataclasses import dataclass
# Create your views here.

def kianu(request):
    @dataclass
    class Kianu:
        year_born: int
        city_born : str
        movie_name: str
    kianu = Kianu(1964,'Бейрут','На гребне волны')
    data = {
        "year_born":kianu.year_born,
        'movie_name':kianu.movie_name,
        'city_born':kianu.city_born,
    }
    return render(request,'different_stuff/kianu.html',context=data)