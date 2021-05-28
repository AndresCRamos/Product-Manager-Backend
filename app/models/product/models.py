from django.db import models
from ..supplier.models import Supplier


class Product(models.Model):
    name = models.CharField(max_length=20)
    sale_value = models.DecimalField(max_digits=10, decimal_places=2)
    no_VAT_value = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_value = models.DecimalField(max_digits=20, decimal_places=2)
    min_quantity = models.IntegerField()
    max_quantity = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
