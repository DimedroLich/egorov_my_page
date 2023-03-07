from django.urls import path
import views
urlpatterns = [
    path('',views.all_horoscope),
    path('<int:sign_zodiac>/',views.get_info_about_zodiac_by_num),
    path('<str:sign_zodiac>/',views.get_info_about_zodiac,name = 'horoscop-name'),
    ]
