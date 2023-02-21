from rest_framework import serializers
from .models import Car

class Car_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id','year','make','model','color']