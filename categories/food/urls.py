from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.food_index, name='food_index'),
    path('<slug:food_slug>/', views.food_shop, name='food_shop'),
]
