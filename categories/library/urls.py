from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.library_index, name='library_index'),
    path('<slug:building_slug>/', views.library_building, name='library_building'),

]
