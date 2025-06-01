from django.urls import path
from . import views

urlpatterns = [
    path('', views.washroom_index, name = "washroom_index")
]
