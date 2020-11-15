# Вступление
Проект создан в рамках хакатона СЕВЕРО-ЗАПАДНЫЙ IT-ХАБ. Кейс SPb-Alert. Здесь представлен backend написанные на python с использованием django.

В данном репозитории хранится код для обработки датасетов и выявления статистический закономерностей в них, api для получения информации клиентом и api для загрузки информации в базу данных в режиме реального времени.
## Документация по API

```http
GET /api/get/?params
```

Возвращает список сообщений о проишествиях фильтруя по params.

| Paramets | Type | Description |
| :--- | :--- | :--- |
| `limit` | `int` or `None` | Ограничивает размер ответа. Default=100 |
| `datetime_lte` | `string` | Фильтр раньше чем ДатаВремя в формате `%d.%m.%Y %H:%M` Default=None |
| `datetime_gte` | `string` | Фильтр позже чем ДатаВремя в формате `%d.%m.%Y %H:%M` Default=None |
| `areas` | `string1,string2...` or `int1,int2...` | Фильтр по районам по названию, либо по id Default=all |
| `cats` | `string1,string2...` or `int1,int2...` | Фильтр по типу проишествия по названию, либо по id Default=all|

### Ответ
```javascript
[
    {
        "id": 1,
        "category": {
            "id": 1,
            "name": "Слабый напор или отсутствие горячего водоснабжения"
        },
        "area": {
            "id": 5,
            "name": "Колпинский"
        },
        "datetime": "15.11.2020 04:45",
        "eas_address": 279466,
        "eas_building": 124061,
        "latitude": 59.918522,
        "longitude": 30.307146,
        "accident": 1
    }
]
```

```http
GET /api/get/?params
```

Возвращает список аварий за последнее время специфичное для типа аварии. Содержит в себе все сообщения о данной аварии (Какие сообщения включать, а какие нет устанавливается статистическими методами специально для данного района и типа аварии). Включает "нормальное" значение для количества сообщений о проишествие в конкретном районе в конкретные часы.

| Paramets | Type | Description |
| :--- | :--- | :--- |
| `areas` | `string1,string2...` or `int1,int2...` | Фильтр по районам по названию, либо по id Default=all |
| `cats` | `string1,string2...` or `int1,int2...` | Фильтр по типу проишествия по названию, либо по id Default=all|

### Ответ
```javascript
[
    {
        "id": 1,
        "datetime": "15.11.2020 04:45",
        "messages": [
            {
                "datetime": "15.11.2020 04:45",
                "latitude": 59.918522,
                "longitude": 30.307146
            }
        ],
        "normal_count": null,
        "duration": 3,
        "longitude": 30.307146,
        "latitude": 59.918522,
        "eas_address": 279466,
        "eas_building": 124061,
        "category": 1,
        "area": 5
    }
]
```

Возвращает сообщения о проишествия фильтруя по params.

| Paramets | Type | Description |
| :--- | :--- | :--- |
| `limit` | `int` or `None` | Ограничивает размер ответа. Default=100 |
| `datetime_lte` | `string` | Фильтр раньше чем ДатаВремя в формате `%d.%m.%Y %H:%M` Default=None |
| `datetime_gte` | `string` | Фильтр позже чем ДатаВремя в формате `%d.%m.%Y %H:%M` Default=None |
| `areas` | `string1,string2...` or `int1,int2...` | Фильтр по районам по названию, либо по id Default=all |
| `cats` | `string1,string2...` or `int1,int2...` | Фильтр по типу проишествия по названию, либо по id Default=all|

### Ответ
```javascript
[
    {
        "id": 1,
        "category": {
            "id": 1,
            "name": "Слабый напор или отсутствие горячего водоснабжения"
        },
        "area": {
            "id": 5,
            "name": "Колпинский"
        },
        "datetime": "15.11.2020 04:45",
        "eas_address": 279466,
        "eas_building": 124061,
        "latitude": 59.918522,
        "longitude": 30.307146,
        "accident": 1
    }
]
```
```

```http
GET /api/get/cats/
```

Возвращает cписок типов проишествий

### Ответ
```javascript
[
    {
        "id": 1,
        "name": "Слабый напор или отсутствие горячего водоснабжения"
    },
    {
        "id": 2,
        "name": "Слабый напор или отсутствие холодного водоснабжения"
    },
    {
        "id": 3,
        "name": "ДТП с пострадавшими людьми"
    },
    {
        "id": 4,
        "name": "Пожары"
    }
]
```

```http
GET /api/get/areas/
```

Возвращает cписок районов

### Ответ
```javascript
[
    {
        "id": 1,
        "name": "Центральный"
    },
    {
        "id": 2,
        "name": "Красногвардейский"
    },
    {
        "id": 3,
        "name": "Петродворцовый"
    },
    {
        "id": 4,
        "name": "Красносельский"
    }
]
```


