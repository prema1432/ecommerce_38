from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    ROLES_CHOICES = (
        ('admin', 'admin'),
        ('customer', 'customer'),
        ('rider', 'rider'),
    )
    phone_number = models.BigIntegerField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    roles = models.CharField(max_length=10, null=True, blank=True, choices=ROLES_CHOICES, default='customer')
