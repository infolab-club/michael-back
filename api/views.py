from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Case, When, F, Value, Q

from .models import *
from .serializers import *

from datetime import datetime
DATETIME_FORMAT = "%d.%m.%Y %H:%M"

class IncidentView(APIView):
    def get(self, request):
        limit = 100
        filter_params = {}
        if request.query_params.get('datetime_lte'):
            filter_params["datetime__lte"] = datetime.strptime(request.query_params['datetime_lte'], DATETIME_FORMAT)
        if request.query_params.get('datetime_gte'):
            filter_params["datetime__gte"] = datetime.strptime(request.query_params['datetime_gte'], DATETIME_FORMAT)
        if request.query_params.get('area'):
            filter_params["area__name__in"] = request.query_params['area'].split(',')
        if request.query_params.get('categoryes'):
            filter_params["categoryes__name__in"] = request.query_params['categoryes'].split(',')
        if request.query_params.get('limit'):
            limit = int(request.query_params['limit'])
        

        incidents = Incident.objects.filter(**filter_params)[:limit]
        serializer = IncidentSerializer(incidents, many=True)
        return Response(serializer.data)