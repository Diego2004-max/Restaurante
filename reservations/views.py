from django.shortcuts import render, redirect
from .models import Reservation
from django.contrib.auth.decorators import login_required

@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, "reservations/list.html", {"reservations": reservations})

@login_required
def reservation_create(request):
    if request.method == "POST":
        Reservation.objects.create(
            user=request.user,
            date=request.POST["date"],
            time=request.POST["time"],
            persons=request.POST["persons"],
            notes=request.POST["notes"]
        )
        return redirect("reservations:list")
    return render(request, "reservations/form.html")
