from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=20, default="unidades")  # gramos, ml, unidades
    quantity = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient, through="DishIngredient")

    def __str__(self):
        return self.name


class DishIngredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField(help_text="Cantidad necesaria del ingrediente")

    def __str__(self):
        return f"{self.amount} de {self.ingredient.name} para {self.dish.name}"
