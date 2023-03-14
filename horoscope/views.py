from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from datetime import date

# Create your views here.

signs = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}

signs_by_dates = {
    tuple(range(date(year=2023,month=3,day=21).toordinal(),date(year=2023,month=4,day=20).toordinal()+1)):"aries",
    tuple(range(date(year=2023,month=4,day=21).toordinal(),date(year=2023,month=5,day=21).toordinal()+1)):"taurus",
    tuple(range(date(year=2023,month=5,day=22).toordinal(),date(year=2023,month=6,day=21).toordinal()+1)):"gemini",
    tuple(range(date(year=2023,month=6,day=22).toordinal(),date(year=2023,month=7,day=22).toordinal()+1)):"cancer",
    tuple(range(date(year=2023,month=7,day=23).toordinal(),date(year=2023,month=8,day=21).toordinal()+1)):"leo",
    tuple(range(date(year=2023,month=8,day=22).toordinal(),date(year=2023,month=9,day=23).toordinal()+1)):"virgo",
    tuple(range(date(year=2023,month=9,day=24).toordinal(),date(year=2023,month=10,day=23).toordinal()+1)):"libra",
    tuple(range(date(year=2023,month=10,day=24).toordinal(),date(year=2023,month=11,day=22).toordinal()+1)):"scorpio",
    tuple(range(date(year=2023,month=11,day=23).toordinal(),date(year=2023,month=12,day=22).toordinal()+1)):"sagittarius",
    tuple(range(date(year=2023,month=12,day=23).toordinal(),date(year=2023,month=1,day=20).toordinal()+1)):"capricorn",
    tuple(range(date(year=2023,month=1,day=21).toordinal(),date(year=2023,month=2,day=19).toordinal()+1)):"aquarius",
    tuple(range(date(year=2023,month=2,day=20).toordinal(),date(year=2023,month=3,day=20).toordinal()+1)):"pisces",
}

elements = {
    "fire": ('Огненные знаки', 'aries', 'leo', 'sagittarius'),
    "earth": ('Знаки земли', "taurus", "virgo", "capricorn"),
    "air": ('Воздушные знаки', "gemini", "libra", "aquarius"),
    "water": ('Водные знаки', "cancer", "scorpio", "pisces"),
}


def index(request):
    signs_ = list(signs)
    signs_template = ""
    for s in signs_:
        url_path = reverse("horoscop-name", args=(s,))
        signs_template += f'<li><a href={url_path}>{s}</a></li>'
    template = f"""
                <h3>Знаки зодиака</h3>
                <ul>
                    {signs_template}
                </ul>
                """
    return HttpResponse(template)


def get_info_about_zodiac(request, sign_zodiac: str):
    description = {
        'zodiac_description' : signs[sign_zodiac],
        'sign':sign_zodiac,
        'int_n': 2,
        'value': 'Django project ebobo',
    }
    return render(request, 'horoscope/info_zodiac.html',context=description)


def get_info_about_zodiac_by_num(request, sign_zodiac: int):
    if not len(signs) >= int(sign_zodiac) >= 1:
        raise Http404(f'Неизвестный знак зодиака {sign_zodiac}')
    signs_ = list(signs)
    current_sign = signs_[sign_zodiac - 1]
    redirect_url = reverse("horoscop-name", args=(current_sign,))
    return HttpResponseRedirect(redirect_url)


def zodiac_types(request):
    all_elem = list(elements)
    elems = ''
    for i in all_elem:
        url = reverse('element', args=(i,))
        elems += f'<li><a href={url}>{i.title()}</a></li>'
    response = f'''
                <h3>Стихии знаков зодиака</h3>
                <ul>
                    {elems}
                </ul>
                '''
    return HttpResponse(response)


def signs_by_element(request, element):
    if not element in elements:
        raise Http404()
    signs = ''
    for elem in elements[element][1:]:
        url = reverse('horoscop-name', args=(elem,))
        signs += f'<li><a href={url}>{elem.title()}</a></li>'
    response = f'''
            <h2>{elements[element][0]}</h2>
            <ul>
                {signs}
            </ul>
            '''
    return HttpResponse(response)


def date_convert(request, month, day):
    from datetime import date
    try:
        dat = date(year=2023,month=month,day=day).toordinal()
        for date_from_base in signs_by_dates:
            if dat in date_from_base:
                return HttpResponse(signs_by_dates[date_from_base].title())
    except ValueError:
        raise Http404()

