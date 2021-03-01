from django.contrib import admin
from django.urls import path, include

from .views import car_list, CarAPIView, CarDetails, GenericAPIView, EmployeeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee', EmployeeViewSet, basename='employee')

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
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>.', include(router.urls))
]