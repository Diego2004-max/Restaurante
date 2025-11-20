from django.db import models
from menu.models import Ingredient
from django.contrib.auth.models import User

class InventoryItem(models.Model):
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE)
    stock = models.FloatField(default=0)

    def __str__(self):
        return f"{self.ingredient.name} - {self.stock} {self.ingredient.unit}"


class StockMovement(models.Model):
    MOV_TYPES = [
        ("IN", "Entrada"),
        ("OUT", "Salida"),
    ]

    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    movement_type = models.CharField(max_length=10, choices=MOV_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.movement_type} {self.quantity} {self.ingredient.name}"
