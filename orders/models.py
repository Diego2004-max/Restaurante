from django.db import models
from django.contrib.auth.models import User
from menu.models import Dish

class Order(models.Model):
    STATUS = [
        ("PENDING", "Pendiente"),
        ("PAID", "Pagado"),
        ("DELIVERED", "Entregado"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS, default="PENDING")

    def __str__(self):
        return f"Orden #{self.id} - {self.user.username}"

    def total(self):
        return sum(item.subtotal() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.quantity * self.dish.price


class Payment(models.Model):
    METHODS = [
        ("CASH", "Efectivo"),
        ("CARD", "Tarjeta"),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    method = models.CharField(max_length=20, choices=METHODS)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago #{self.id} - Orden {self.order.id}"
