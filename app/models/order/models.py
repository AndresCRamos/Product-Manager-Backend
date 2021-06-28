from django.db import models
from ..seller.models import Seller
from ..client.models import Client
from ..product.models import Product


class Order(models.Model):
    class StateChoices(models.TextChoices):
        WAIT = 'Wait'
        PACKAGING = 'Packaging'
        SENT = 'Sent'
        DELIVERED = 'Delivered'

    order_date = models.DateField(auto_now=True)
    max_deliver_date = models.DateField(auto_now_add=False)
    state = models.CharField(
        max_length=15,
        choices=StateChoices.choices,
        default=StateChoices.WAIT
    )
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)


class OrderedProduct(models.Model):
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
