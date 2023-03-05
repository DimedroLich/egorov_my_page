from django.urls import path
import week_days.views as v

urlpatterns = [
    path('',v.main),
    path('monday/', v.mon),
    path('tuesday/', v.tuesday),
]
