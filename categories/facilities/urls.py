from django.urls import path
from . import views

urlpatterns = [
    path('', views.facilities_index, name='facilities_index'),
    path('<slug:slug>/', views.facilities_detail, name='facilities_detail'),
]
