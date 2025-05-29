from django.urls import path
from . import views

urlpatterns = [
    path("", views.bank_index, name = "bank_index"),
]
