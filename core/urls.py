from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.core_index, name='core_index'),
      # Category routes
    path('academic/', include('categories.academic.urls')),
    path('hostel/', include('categories.hostels.urls')),
    path('library/', include('categories.library.urls')),
    path('food/', include('categories.food.urls')),
    path('shop/', include('categories.shop.urls')),
    path('health/', include('categories.health_center.urls')),
    path('bank/', include('categories.bankATM.urls')),
    path('parking/', include('categories.parking_area.urls')),
    path('auditorium/', include('categories.auditorium.urls')),
    path('sports/', include('categories.sports.urls')),
    path('faculty/', include('categories.faculty_office.urls')),
#     path('residential/', include('categories.residential.urls')),
#     path('essentials/', include('categories.essentials.urls')),
#     path('helpinfo/', include('categories.helpinfo.urls')),
#     path('adminservices/', include('categories.adminservices.urls')),
#     path('facilities/', include('categories.facilities.urls')),
#     path('<slug:slug>/', views.core_detail, name='core_detail'),
]
