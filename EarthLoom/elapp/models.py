
from django.db import models

class UserRegistration(models.Model):
    USER_TYPES = [
        ('farmer', 'Farmer'),
        ('customer', 'Customer'),
    ]
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    def __str__(self):
        return self.username
