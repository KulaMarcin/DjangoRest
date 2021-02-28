from django.contrib import admin
from django.urls import path

from .views import car_list, car_detail

urlpatterns = [
    path('car/', car_list),
    path('detail/<int:pk>/', car_detail)
]