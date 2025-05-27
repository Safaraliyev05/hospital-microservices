from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class User(AbstractUser):
    ROLE_CHOICES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('admin', 'Admin'),
    ]

    phone = CharField(max_length=15, blank=True, null=True)
    role = CharField(max_length=10, choices=ROLE_CHOICES, default='patient')

    def __str__(self):
        return self.username
