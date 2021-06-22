from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class Employee(AbstractUser):
    class EmployeeType(models.TextChoices):
        ADMIN = 'Admin'
        CONVEYOR = 'Conveyor'
        SELLER = 'Seller'
        ACCOUNTANT = 'Accountant'

    username = None
    id_card = models.BigIntegerField(null=False, primary_key=True)
    email = models.EmailField(unique=True)
    cellphone = models.BigIntegerField(null=False)
    city = models.CharField(max_length=20, null=False)
    neighborhood = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=20, null=False)
    type = models.CharField(
        max_length=10,
        choices=EmployeeType.choices,
        null=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['id_card', 'cellphone', 'city', 'neighborhood', 'address', 'type']

    objects = CustomUserManager()
