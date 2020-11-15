import pandas as pd
import numpy as np
from api.models import *
from datetime import datetime
from django.utils.timezone import make_aware

def get_ids(lst, model):
    dc = {}
    for name in lst:
        id_tuple = model.objects.get_or_create(name=name)
        if id_tuple[0]:
            dc[name] = id_tuple[0].id
        else:
            dc[name] = id_tuple[1].id
    return dc

def parseDatasetToBd(dataset, datetime_format):
    dataset = pd.read_excel(dataset, date_parser=(lambda st: datetime.strptime(st, datetime_format)), converters={'Идентификатор Еас здания': int, 'Идентификатор Еас адреса': int, 'Широта': float, 'Долгота': float})
    categoryes = dataset['Категория'].unique()
    areas = dataset['Район'].unique()

    categoryes = get_ids(categoryes, Category)
    areas = get_ids(areas, Area)
    
    dataset['Категория'] = dataset['Категория'].apply((lambda name: categoryes[name]))
    dataset['Район'] = dataset['Район'].apply(lambda name: areas[name])
    dataset['Идентификатор Еас адреса'] = dataset['Идентификатор Еас адреса'].apply(lambda x: x if x is not np.nan else 0)
    dataset['Идентификатор Еас здания'] = dataset['Идентификатор Еас здания'].apply(lambda x: x if x is not np.nan else 0)
    for index, row in dataset.iloc[1:].iterrows():
        Message.objects.create(category=Category.objects.get(id=row['Категория']), area=Area.objects.get(id=row['Район']), latitude=row['Широта'],
            longitude=row['Долгота'], eas_address=row['Идентификатор Еас адреса'],
            eas_building=row['Идентификатор Еас здания'], datetime=row['Время регистрации'])