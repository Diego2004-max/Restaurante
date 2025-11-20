from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20, default="unidad")
    quantity = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    ingredients = models.ManyToManyField(Ingredient, blank=True)

    def __str__(self):
        return self.name
