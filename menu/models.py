from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=20, default="unidades")  # gramos, ml, unidades
    quantity = models.FloatField(default=0)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Precio (COP)"
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through="DishIngredient",
        related_name="used_in"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} — COP {self.price}"


class DishIngredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField(help_text="Cantidad necesaria del ingrediente")

    class Meta:
        verbose_name = "Ingrediente del plato"
        verbose_name_plural = "Ingredientes de platos"
        unique_together = ("dish", "ingredient")

    def __str__(self):
        return f"{self.amount} de {self.ingredient.name} para {self.dish.name}"
