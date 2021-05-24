from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    email = models.EmailField()