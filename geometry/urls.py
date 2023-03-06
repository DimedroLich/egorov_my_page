from django.urls import path
from . import views
urlpatterns = [
    path('rectangle/<int:width>/<int:height>',views.rect),
    path("square/<int:width>",views.square),
    path('circle/<int:radius>',views.circle),
]