from django.db import models
from app.models.purchase.models import Purchase


class PurchaseOnCredit(models.Model):
    purchase = models.OneToOneField(Purchase, on_delete=models.CASCADE)
    state = models.CharField(max_length=10)
    max_payment_date = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False)
    payment_date = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False)


