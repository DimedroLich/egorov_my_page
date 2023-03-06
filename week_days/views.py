from django.shortcuts import render, HttpResponse, Http404


# Create your views here.
def main(request):
    return HttpResponse('Задачи по дням недели')


weekdays = {
    'monday': '<h2>Дела на понедельник</h2>'
              '<p>1) Анжуманя</p>',
    'tuesday': '<h2>Дела на Вторник</h2>'
               '<p>1) Пресс качат</p>',
    'wednesday': '<h2>Дела на среду</h2>'
                 '<p>1) Кросс бегит</p>',
    'thursday': '<h2>Дела на четверг</h2>'
                '<p>1) Жопа приседат</p>',
    'friday': '<h2>Дела на пятницу</h2>'
              '<p>1) Анжуманя</p>',
    'saturday': '<h2>Дела на субботу</h2>'
                '<p>1) отдых</p>',
    'sunday': '<h2>Дела на восрксенье</h2>'
              '<p>1) Английский посещат</p>',
}


def days(request, weekday):
    if weekday in weekdays:
        return HttpResponse(weekdays[weekday])
    else:
        raise Http404('Проверьте правильность дня недели')


def days_by_n(request, weekday: int):
    if 7 >= weekday >= 1:
        return HttpResponse(f'Сегодня {weekday} день недели')
    else:
        raise Http404(f'Неверный номер дня - {weekday}')