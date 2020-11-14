from rest_framework import serializers
from .models import *

DATETIME_FORMAT = "%d.%m.%Y %H:%M"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        exclude = []


class IncidentSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    area = AreaSerializer()
    datetime = serializers.DateTimeField(format=DATETIME_FORMAT)
    class Meta:
        model = Incident
        exclude = []