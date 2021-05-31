from django.db import models
from ..employee.models import Employee
from ..zone.models import Zone


class Seller(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, null=False)
    zone = models.ForeignKey(Zone, on_delete=models.DO_NOTHING, null=False)
