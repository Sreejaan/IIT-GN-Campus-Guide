from django.urls import path
from . import views

urlpatterns = [
    path('', views.auditorium_index, name='auditorium_index'),
    path('<slug:auditorium_slug>/', views.auditorium_detail, name='auditorium_detail'),  # This one must exist!
]