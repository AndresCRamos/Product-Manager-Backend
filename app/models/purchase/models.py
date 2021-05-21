from django.db import models
from app.models.supplier.models import Supplier


class Purchase(models.Model):
    buy_date = models.DateField(auto_now=True, auto_now_add=False)
    deliver_date = models.DateField(auto_now=True, auto_now_add=False, default=None, blank=True, null=True)
    value = models.DecimalField(decimal_places=2, max_digits=10)
    payment_type = models.CharField(max_length=10, default='now')
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
