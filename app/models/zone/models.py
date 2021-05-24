from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=20)
    neighborhood = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
