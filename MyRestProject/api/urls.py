from django.contrib import admin
from django.urls import path

from .views import car_list

urlpatterns = [
    path('car/', car_list)
]