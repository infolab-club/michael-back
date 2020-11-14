from django.db import models




class Category(models.Model):   
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Incident(models.Model):
    datetime = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="incidents")
    eas_address = models.IntegerField()
    eas_building = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="incidents")