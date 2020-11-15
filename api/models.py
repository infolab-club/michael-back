from django.db import models


class Category(models.Model):   
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class NormalCount(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="normals")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="normals")
    value = models.IntegerField(default=0)


class Accident(models.Model):
    datetime = models.DateTimeField()
    duration = models.IntegerField(default=3)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="accidents", null=True, blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="accidents", null=True, blank=True)
    eas_address = models.IntegerField()
    eas_building = models.IntegerField()


class Message(models.Model):
    datetime = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="messages")
    eas_address = models.IntegerField()
    eas_building = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="message", null=True, blank=True)
    accident = models.ForeignKey(Accident, on_delete=models.CASCADE, related_name="messages", null=True, blank=True)


