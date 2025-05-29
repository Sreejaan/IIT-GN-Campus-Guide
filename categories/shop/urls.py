from django.urls import path
from . import views

urlpatterns = [
    path("", views.shop_index, name = "shop_index"),
    path("<slug:shop_slug>", views.shop_detail, name = "shop_detail"),

]
