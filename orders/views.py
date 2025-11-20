from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from menu.models import Dish
from .models import Order, OrderItem, Payment
from core.decorators import role_required


@login_required
@role_required(["admin", "mesero", "cliente"])
def menu_view(request):
    dishes = Dish.objects.all()
    return render(request, "orders/menu.html", {"dishes": dishes})


@login_required
@role_required(["admin", "mesero", "cliente"])
def add_to_cart(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)

    order, created = Order.objects.get_or_create(
        user=request.user,
        status="PENDING",
    )

    item, created = OrderItem.objects.get_or_create(order=order, dish=dish)
    item.quantity += 1
    item.save()

    return redirect("orders:cart")


@login_required
@role_required(["admin", "mesero", "cliente"])
def cart(request):
    order = Order.objects.filter(user=request.user, status="PENDING").first()
    return render(request, "orders/cart.html", {"order": order})


@login_required
@role_required(["admin", "mesero", "cliente"])
def pay_order(request):
    order = get_object_or_404(Order, user=request.user, status="PENDING")

    Payment.objects.create(
        order=order,
        method="CASH",
        amount=order.total(),
    )

    order.status = "PAID"
    order.save()

    return redirect("orders:history")


@login_required
@role_required(["admin", "mesero"])
def history(request):
    orders = Order.objects.filter(user=request.user).exclude(status="PENDING")
    return render(request, "orders/history.html", {"orders": orders})
