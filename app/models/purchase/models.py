from django.db import models
from ..supplier.models import Supplier


class Purchase(models.Model):

    class PaymentType(models.TextChoices):
        NOW = 'NOW', 'Pago de contado',
        CREDIT = 'CR', 'Pago a credito'

    buy_date = models.DateField(auto_now=True, auto_now_add=False)
    deliver_date = models.DateField(default=None, blank=True, null=True)
    value = models.DecimalField(decimal_places=2, max_digits=10)
    payment_type = models.CharField(
        max_length=10,
        choices=PaymentType.choices,
        default=PaymentType.NOW
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
