from django.db import models
from django.contrib.auth.models import User
from view_table.models import ViewTable


class EmployeeType(models.TextChoices):
    CONVEYOR = '0', 'Conveyor'
    SELLER = '1', 'Seller'
    ACCOUNTANT = '2', 'Accountant'


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_card = models.BigIntegerField(null=False, unique=True)
    cellphone = models.BigIntegerField(null=False)
    city = models.CharField(max_length=20, null=False)
    neighborhood = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=20, null=False)
    type = models.CharField(
        max_length=2,
        choices=EmployeeType.choices,
        default=EmployeeType.ACCOUNTANT,
        null=False
    )
