from django.urls import path
from . import views

urlpatterns = [
    path('', views.academic_index, name='academic_index'),
    # path('<slug:slug>/', views.academic_detail, name='academic_detail'),
    path('<slug:building_slug>/', views.academic_building, name='academic_building'),
]
