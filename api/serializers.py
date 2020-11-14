from rest_framework import serializers
from .models import *

DATETIME_FORMAT = "%d.%m.%Y %H:%M"

class IncidentSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    area = serializers.StringRelatedField()
    datetime = serializers.DateTimeField(format=DATETIME_FORMAT)
    class Meta:
        model = Incident
        exclude = []


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []