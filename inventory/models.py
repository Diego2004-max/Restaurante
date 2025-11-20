from django.db import models
from django.conf import settings

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=20, default="unidad")

    def __str__(self):
        return self.name

class StockMovement(models.Model):
    MOV_TYPES = (
        ("in", "Entrada"),
        ("out", "Salida"),
    )
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    movement_type = models.CharField(max_length=3, choices=MOV_TYPES)
    quantity = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item.name} - {self.movement_type}"
