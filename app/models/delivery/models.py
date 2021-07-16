from django.db import models
from ..order.models import Order
from ..conveyor.models import Conveyor
from ..vehicle.models import Vehicle


class Delivery(models.Model):

    class StateChoices(models.TextChoices):
        PACKAGING = 'Packaging'
        SENT = 'Sent'
        DELIVERED = 'Delivered'

    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=StateChoices.choices,
        default=StateChoices.PACKAGING,
        null=False
    )
    bill = models.IntegerField(null=False)
    conveyor = models.ForeignKey(Conveyor, on_delete=models.DO_NOTHING)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING)
