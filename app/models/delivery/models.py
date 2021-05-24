from django.db import models
from app.models.order.models import Order
from app.models.conveyor.models import Conveyor
from app.models.vehicle.models import Vehicle


class Delivery(models.Model):

    class StateChoices(models.TextChoices):
        PACKAGING = 'Pack', 'Empacando'
        SENT = 'Sent', 'Enviado'
        DELIVERED = 'Del', 'Entregado'

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
