from django.urls import path
import week_days.views as v

urlpatterns = [
    path('',v.main),
    path('<int:weekday>/', v.days_by_n),
    path('<str:weekday>/', v.days),
]
