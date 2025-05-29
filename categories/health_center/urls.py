from django.urls import path
from . import views

urlpatterns = [
    path("", views.health_index, name = "health_index")
]
