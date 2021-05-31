from django.db import models
from ..zone.models import Zone


class Client(models.Model):
    id_card = models.BigIntegerField(null=False, unique=True)
    name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    telephone = models.BigIntegerField(null=False)
    cellphone = models.BigIntegerField()
    address = models.CharField(max_length=100, null=False)
    zone = models.ForeignKey(Zone, on_delete=models.DO_NOTHING, null=False)

