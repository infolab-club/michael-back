from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Case, When, F, Value, Q

from .models import *
from .serializers import *

from datetime import datetime, timedelta

from .service import updateAccidentOrCreate


DATETIME_FORMAT = "%d.%m.%Y %H:%M"

class MessageView(APIView):
    def get(self, request):
        limit = 100
        filter_params = {}
        if request.query_params.get('datetime_lte'):
            filter_params["datetime__lte"] = datetime.strptime(request.query_params['datetime_lte'], DATETIME_FORMAT)
        if request.query_params.get('datetime_gte'):
            filter_params["datetime__gte"] = datetime.strptime(request.query_params['datetime_gte'], DATETIME_FORMAT)

        if request.query_params.get('areas'):
            tmp = request.query_params['areas'].split(',')
            filter_params["area__name__in"] = []
            filter_params["area__id__in"] = []
            for cat in tmp:
                try:
                    filter_params["area__id__in"].append(int(cat.strip()))
                except:
                    filter_params["area__id__in"].append(cat.strip())
            if not filter_params["area__id__in"]:
                del filter_params["area__id__in"]
            if not filter_params["area__name__in"]:
                del filter_params["area__name__in"]

        if request.query_params.get('cats'):
            tmp = request.query_params['cats'].split(',')
            filter_params["category__id__in"] = []
            filter_params["category__name__in"] = []
            for cat in tmp:
                try:
                    filter_params["category__id__in"].append(int(cat.strip()))
                except:
                    filter_params["category__name__in"].append(cat.strip())
            if not filter_params["category__name__in"]:
                del filter_params["category__name__in"]
            if not filter_params["category__id__in"]:
                del filter_params["category__id__in"]


        if request.query_params.get('limit'):
            if request.query_params.get('limit').lower() == 'none':
                limit = None
            else:
                limit = int(request.query_params['limit'])
        

        messages = Message.objects.filter(**filter_params)[:limit]
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


class CategoryView(APIView):
    def get(self, request):
        categoryes = Category.objects.all()
        serializer = CategorySerializer(categoryes, many=True)
        return Response(serializer.data)


class AreaView(APIView):
    def get(self, request):
        areas = Area.objects.all()
        serializer = AreaSerializer(areas, many=True)
        return Response(serializer.data)


class MessageRegisterView(APIView):
    def post(self, request):
        message = MessageRegisterSerializer(data=request.data)
        if message.is_valid():
            message = message.save()
            updateAccidentOrCreate(message)
            return Response('Success')
        else:
            return Response(message.errors)


class AccidentView(APIView):
    def get(self, request):
        filter_params = {}
        if request.query_params.get('cats'):
            tmp = request.query_params['cats'].split(',')
            filter_params["category__id__in"] = []
            filter_params["category__name__in"] = []
            for cat in tmp:
                try:
                    filter_params["category__id__in"].append(int(cat.strip()))
                except:
                    filter_params["category__name__in"].append(cat.strip())
            if not filter_params["category__name__in"]:
                del filter_params["category__name__in"]
            if not filter_params["category__id__in"]:
                del filter_params["category__id__in"]
        
        if request.query_params.get('areas'):
            tmp = request.query_params['areas'].split(',')
            filter_params["area__name__in"] = []
            filter_params["area__id__in"] = []
            for cat in tmp:
                try:
                    filter_params["area__id__in"].append(int(cat.strip()))
                except:
                    filter_params["area__id__in"].append(cat.strip())
            if not filter_params["area__id__in"]:
                del filter_params["area__id__in"]
            if not filter_params["area__name__in"]:
                del filter_params["area__name__in"]
        
        accidents = Accident.objects.filter(**filter_params).filter(datetime__gte=datetime.now() - timedelta(hours=3))
        serializer = AccidentSerializer(accidents, many=True)
        return Response(serializer.data)