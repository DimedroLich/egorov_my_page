from django.urls import path
import views
urlpatterns = [
    path('',views.index,name='horoscope_main'),
    path('type/', views.zodiac_types),
    path('type/<element>', views.signs_by_element,name = 'element'),
    path('<int:month>/<int:day>',views.date_convert),
    path('<int:sign_zodiac>/',views.get_info_about_zodiac_by_num),
    path('<str:sign_zodiac>/',views.get_info_about_zodiac,name = 'horoscop-name'),

    ]
