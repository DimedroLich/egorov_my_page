from django.urls import path
import week_days.views as v

urlpatterns = [
    path('',v.main),
    path('<weekday>/', v.days),
]
