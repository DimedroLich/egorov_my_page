from django.urls import path
from . import views
urlpatterns = [
    path('kianu/',views.kianu),
    path('guiness/',views.get_guinness_world_records)
]