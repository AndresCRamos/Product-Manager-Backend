from django.db import models
from ..seller.models import Seller
from ..client.models import Client


class Order(models.Model):

    class StateChoices(models.TextChoices):
        WAIT = 'Wait', 'En espera'
        PACKAGING = 'Packaging', 'Empacando'
        SENT = 'Sent', 'Enviado'
        DELIVERED = 'Delivered', 'Entregado'

    order_date = models.DateField(auto_now=True, auto_now_add=False)
    deliver_date = models.DateField(auto_now=False, auto_now_add=False, null=False)
    total_value = models.DecimalField(max_digits=100, decimal_places=2, null=False)
    state = models.CharField(
        max_length=15,
        choices=StateChoices.choices,
        default=StateChoices.WAIT
    )
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
