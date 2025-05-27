from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.core_index, name='core_index'),
      # Category routes
    path('academic/', include('categories.academic.urls'), name = "academic"),
    path('hostel/', include('categories.hostels.urls'), name = 'hostel'),

#     path('residential/', include('categories.residential.urls')),
#     path('essentials/', include('categories.essentials.urls')),
#     path('helpinfo/', include('categories.helpinfo.urls')),
#     path('adminservices/', include('categories.adminservices.urls')),
#     path('facilities/', include('categories.facilities.urls')),
#     path('<slug:slug>/', views.core_detail, name='core_detail'),
]
