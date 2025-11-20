from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Reservation
from core.decorators import role_required


@login_required
@role_required(["cliente", "admin"])
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, "reservations/list.html", {"reservations": reservations})


@login_required
@role_required(["cliente", "admin"])
def reservation_create(request):
    if request.method == "POST":
        Reservation.objects.create(
            user=request.user,
            date=request.POST.get("date"),
            time=request.POST.get("time"),
            persons=request.POST.get("persons"),
            notes=request.POST.get("notes"),
        )
        return redirect("reservations:list")

    return render(request, "reservations/form.html")
