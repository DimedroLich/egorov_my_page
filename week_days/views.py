from django.shortcuts import render,HttpResponse

# Create your views here.
def main(request):
    return HttpResponse('Задачи по дням недели')

def mon(request):
    return HttpResponse('<h1>Список дел на понедельник:</h1>'
                        '<p>1) Анжуманя </p>')

def tuesday(request):
    return HttpResponse('<h1>Список дел на вторник:</h1>'
                        '<p>1) Пресс качат </p>'
                        '<p>2) Кросс бегит </p>')