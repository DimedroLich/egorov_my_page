from django.urls import path
from . import views
urlpatterns = [
    path('kianu/',views.kianu),
    path('guiness/',views.get_guinness_world_records),
    path('people/',views.people),
    path('people_detail/',views.people_detail),
    path('beautiful_table/', views.bt_table),
]