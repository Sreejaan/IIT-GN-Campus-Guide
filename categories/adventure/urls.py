from django.urls import path
from . import views

urlpatterns = [
    path('', views.academic_index, name='adventure_index'),
    path('<slug:slug>/', views.academic_detail, name='academic_detail'),
]
