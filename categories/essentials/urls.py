from django.urls import path
from . import views

urlpatterns = [
    path('', views.essentials_index, name='essentials_index'),
    path('<slug:slug>/', views.essentials_detail, name='essentials_detail'),
]
