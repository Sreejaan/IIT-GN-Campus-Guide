from django.urls import path
from . import views

urlpatterns = [
    path('', views.hostel_index, name='hostel_index'),
    path('<slug:building_slug>/', views.hostel_building, name='hostel_building'),
    path('<slug:building_slug>/<str:place_type>/', views.hostel_place_type, name='hostel_place_type'),
    path('<slug:building_slug>/<str:place_type>/<slug:location_slug>/', views.hostel_location_detail, name='hostel_location_detail'),
]
