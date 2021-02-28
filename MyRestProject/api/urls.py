from django.contrib import admin
from django.urls import path

from .views import car_list, CarAPIView, CarDetails

urlpatterns = [
    # for api_view based functions
    # path('car/', car_list),
    # path('detail/<int:pk>/', car_detail),
    path('car/', CarAPIView.as_view()),
    path('detail/<id>/', CarDetails.as_view())
]