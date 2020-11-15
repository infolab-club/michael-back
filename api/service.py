from .models import *
from django.db.models import Case, When, F, Value, Q
from datetime import timedelta, datetime
LONLATDELTA = float(0.01)

def updateAccidentOrCreate(message):


    accident = Accident.objects.filter(
        Q(category=message.category) &
        Q(area=message.area)
    ).filter(
        Q(latitude__gte=message.latitude + LONLATDELTA) &
        Q(latitude__lte=message.latitude - LONLATDELTA) &
        Q(longitude__gte=message.longitude + LONLATDELTA) &
        Q(longitude__lte=message.longitude - LONLATDELTA) &
        Q(datetime__gte=datetime.now() - timedelta(hours=3))
    ).first()
    
    # If already exists
    if accident:
        pass
    else:
        accident = Accident()
        accident.latitude = message.latitude
        accident.longitude = message.longitude
        accident.datetime = message.datetime
        accident.eas_address = message.eas_address
        accident.eas_building = message.eas_building
        accident.category = message.category
        accident.area = message.area
    
    accident.save()
    message.accident = accident
    message.save()