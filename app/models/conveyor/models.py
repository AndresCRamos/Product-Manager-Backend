from django.db import models
from app.models.employee.models import Employee
from app.models.zone.models import Zone


class Conveyor(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, null=False)
    zone = models.ForeignKey(Zone, on_delete=models.DO_NOTHING, null=False)
