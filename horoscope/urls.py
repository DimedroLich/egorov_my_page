from django.urls import path
import views
urlpatterns = [
    path('',views.all_horoscope),
    path('<sign_zodiac>/',views.get_info_about_zodiac),
]
