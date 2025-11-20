from django.shortcuts import render, redirect, get_object_or_404
from .models import InventoryItem, StockMovement
from django.contrib.auth.decorators import login_required


@login_required
def inventory_list(request):
    items = InventoryItem.objects.all()
    return render(request, "inventory/list.html", {"items": items})


@login_required
def movement_create(request):
    items = InventoryItem.objects.all()

    if request.method == "POST":
        item = get_object_or_404(InventoryItem, id=request.POST.get("item"))

        StockMovement.objects.create(
            item=item,
            quantity=float(request.POST.get("quantity")),
            movement_type=request.POST.get("movement_type"),
            user=request.user
        )

        return redirect("inventory:list")

    return render(request, "inventory/movement_form.html", {"items": items})
