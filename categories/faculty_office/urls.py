from django.urls import path
from . import views

urlpatterns = [
    path('', views.academic_index, name='faculty_index'),
    path('<slug:slug>/', views.academic_detail, name='academic_detail'),
]
