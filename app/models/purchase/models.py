from django.db import models
from ..supplier.models import Supplier
from ..product.models import Product


class Purchase(models.Model):

    class PaymentType(models.TextChoices):
        NOW = 'Immediate'
        CREDIT = 'Credit'

    buy_date = models.DateField(auto_now=True, auto_now_add=False)
    deliver_date = models.DateField(default=None, blank=True, null=True)
    value = models.DecimalField(decimal_places=2, max_digits=10)
    payment_type = models.CharField(
        max_length=10,
        choices=PaymentType.choices,
        default=PaymentType.NOW
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)


class PurchasedProduct(models.Model):
    quantity = models.IntegerField(default=1)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = [['purchase', 'product']]


