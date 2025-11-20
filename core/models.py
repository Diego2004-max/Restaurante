from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLES = [
        ("ADMIN", "Administrador"),
        ("WAITER", "Mesero"),
        ("CLIENT", "Cliente"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLES, default="CLIENT")

    def __str__(self):
        return f"{self.user.username} ({self.role})"
