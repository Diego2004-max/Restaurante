from django.shortcuts import render, redirect
from .models import Dish, Ingredient

def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, "menu/dish_list.html", {"dishes": dishes})

def dish_create(request):
    if request.method == "POST":
        Dish.objects.create(
            name=request.POST["name"],
            description=request.POST["description"],
            price=request.POST["price"],
        )
        return redirect("menu:dish_list")
    return render(request, "menu/dish_form.html")


def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, "menu/ingredient_list.html", {"ingredients": ingredients})

def ingredient_create(request):
    if request.method == "POST":
        Ingredient.objects.create(
            name=request.POST["name"],
            unit=request.POST["unit"],
            quantity=request.POST["quantity"]
        )
        return redirect("menu:ingredient_list")
    return render(request, "menu/ingredient_form.html")
