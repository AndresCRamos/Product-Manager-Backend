from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):

    class EmployeeType(models.TextChoices):
        CONVEYOR = 'Conveyor', 'Transportador'
        SELLER = 'Seller', 'Vendedor'
        ACCOUNTANT = 'Accountant', 'Contador'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_card = models.BigIntegerField(null=False, unique=True)
    cellphone = models.BigIntegerField(null=False)
    city = models.CharField(max_length=20, null=False)
    neighborhood = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=20, null=False)
    employee_type = models.CharField(
        max_length=20,
        choices=EmployeeType.choices,
        default=EmployeeType.ACCOUNTANT,
        null=False
    )
