from django.urls import path
from . import views

urlpatterns = [
    path('', views.helpinfo_index, name='helpinfo_index'),
    path('<slug:slug>/', views.helpinfo_detail, name='helpinfo_detail'),
]
