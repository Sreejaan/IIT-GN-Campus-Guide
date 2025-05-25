from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminservices_index, name='adminservices_index'),
    path('<slug:slug>/', views.adminservices_detail, name='adminservices_detail'),
]
