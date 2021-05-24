from django.db import models
from app.models.order.models import Order


class CanceledOrder(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    cancellation_date = models.DateField(auto_now=True, auto_now_add=False, null=False)
    reason = models.TextField()
