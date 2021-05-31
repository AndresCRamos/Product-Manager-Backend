from django.db import models
from ..purchase.models import Purchase


class PurchaseOnCredit(models.Model):

    class PurchaseChoice(models.TextChoices):
        RECEIVED = 'REC', 'Recibido'
        SENT = 'SENT', 'Enviado'
        WAIT = 'WAIT', 'En espera'

    purchase = models.OneToOneField(Purchase, on_delete=models.CASCADE)
    state = models.CharField(
        max_length=10,
        choices=PurchaseChoice.choices,
        default=PurchaseChoice.WAIT
    )
    max_payment_date = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False)
    payment_date = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False)
