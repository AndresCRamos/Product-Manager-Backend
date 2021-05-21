from django.db import models


class Vehicle(models.Model):
    license_plate = models.CharField(max_length=10)
    manufacturer = models.CharField(max_length=100)
    color = models.CharField(max_length=30)
    model = models.IntegerField()
