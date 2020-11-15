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


class MessageSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    area = AreaSerializer()
    datetime = serializers.DateTimeField(format=DATETIME_FORMAT)
    class Meta:
        model = Message
        exclude = []


class MessageRegisterSerializer(serializers.ModelSerializer):
    datetime = serializers.DateTimeField(format=DATETIME_FORMAT, input_formats=[DATETIME_FORMAT])
    class Meta:
        model = Message
        exclude = ['id']


# class NormalCountSerializer(serializers.Serializer):
#     def to_representation(self, value):
#         serializer = self.parent.category.normal.__class__(value, context=self.context)
#         return serializer.data


class MessAccSerializer(serializers.ModelSerializer):
    datetime = serializers.DateTimeField(format=DATETIME_FORMAT)
    class Meta:
        model = Message
        fields = ['datetime', 'latitude', 'longitude']


class AccidentSerializer(serializers.ModelSerializer):
    datetime = serializers.DateTimeField(format=DATETIME_FORMAT)
    messages = MessAccSerializer(many=True)
    normal_count = serializers.SerializerMethodField()
    class Meta:
        model = Accident
        exclude = []

    def get_normal_count(self, obj):
        n_obj = NormalCount.objects.filter(area=obj.area, category=obj.category).first()
        if not n_obj:
            return None
        else:
            return n_obj.value