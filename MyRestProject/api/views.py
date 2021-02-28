from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import JSONParser

from MyRestProject.api.models import Car
from MyRestProject.api.serializers import CarSerializer


def car_list(request):

    if request == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request == 'POST':
        data = JSONParser().parse(request)
        serializer = CarSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
