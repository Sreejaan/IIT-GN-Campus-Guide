# parking_area/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.parking_index, name='parking_index'),
    path('<slug:parking_slug>/', views.parking_detail, name='parking_detail'),
]
