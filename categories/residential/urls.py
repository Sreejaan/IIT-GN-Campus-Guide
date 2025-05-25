from django.urls import path
from . import views

urlpatterns = [
    path('', views.residential_index, name='residential_index'),
    path('<slug:slug>/', views.residential_detail, name='residential_detail'),
]
