from django.urls import path
from . import views

urlpatterns = [
    path('', views.faculty_index, name='faculty_index'),

    # Person detail by slug
    path('person/<slug:slug>/', views.faculty_detail, name='faculty_detail'),

    # Department detail by department code (slug)
    path('department/<slug:code>/', views.department_detail, name='department_detail'),
]
