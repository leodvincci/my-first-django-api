from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import request,JsonResponse
from .serializer import Car_Serializer
from .models import Car

@api_view(["GET"])
def get_all_cars(request):
    my_cars = Car.objects.all()
    car_seri = Car_Serializer(my_cars,many = True)
    return JsonResponse(car_seri.data,safe=False)

@api_view(["POST"])
def add_new_car(request):
    car_seri = Car_Serializer(data=request.data)
    if car_seri.is_valid():
        car_seri.save()
        return Response(car_seri.data,status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def remove_car(request,id):
    print("\nHELHJSLKEFJSLDKJFSLDKJFLDJLJ\n")
    my_car = Car.objects.get(pk=id)
    print("\n\nHELHJ867543245675435645354654324356LDJLJ\n\n")
    my_car.delete()
    return Response("Removed",status=status.HTTP_200_OK)