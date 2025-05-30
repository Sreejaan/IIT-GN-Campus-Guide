from django.urls import path
from . import views

urlpatterns = [
    path('', views.sports_index, name = 'sports_index'),
    path('<slug:sport_slug>', views.sport_detail, name = 'sport_detail'),
]
