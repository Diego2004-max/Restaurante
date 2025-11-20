from django.shortcuts import render, redirect
from .models import InventoryItem, StockMovement
from menu.models import Ingredient
from django.contrib.auth.decorators import login_required

@login_required
def inventory_list(request):
    items = InventoryItem.objects.all()
    return render(request, "inventory/list.html", {"items": items})

@login_required
def movement_create(request):
    ingredients = Ingredient.objects.all()
    if request.method == "POST":
        ingredient = Ingredient.objects.get(id=request.POST["ingredient"])
        mov = StockMovement.objects.create(
            ingredient=ingredient,
            quantity=float(request.POST["quantity"]),
            movement_type=request.POST["movement_type"],
            user=request.user
        )
        return redirect("inventory:list")
    return render(request, "inventory/movement_form.html", {"ingredients": ingredients})
