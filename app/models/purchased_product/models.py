from django.db import models
from ..purchase.models import Purchase
from ..product.models import Product


class PurchasedProduct(models.Model):
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

