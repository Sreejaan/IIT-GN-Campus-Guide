from django.urls import path
from . import views

urlpatterns = [
    path('', views.water_index, name = "water_index"),
]
