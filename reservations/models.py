from django.db import models
from django.conf import settings

class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Reserva de {self.user.username} el {self.date}"
