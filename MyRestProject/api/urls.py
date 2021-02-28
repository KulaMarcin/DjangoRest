from django.contrib import admin
from django.urls import path

from .views import car_list, CarAPIView, CarDetails, GenericAPIView

urlpatterns = [
    # for api_view based functions
    # path('car/', car_list),
    # path('detail/<int:pk>/', car_detail),
    # car used api views
    path('car/', CarAPIView.as_view()),
    path('detail/<id>/', CarDetails.as_view()),
    # person used generic views
    path('person/', GenericAPIView.as_view()),
    path('person/<id>/', GenericAPIView.as_view()),

]