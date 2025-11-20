from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from core.models import Profile

def home(request):
    return render(request, "core/home.html")

def login_view(request):
    if request.method == "POST":
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user:
            login(request, user)
            return redirect("core:dashboard")
        return render(request, "core/login.html", {"error": "Credenciales incorrectas"})
    return render(request, "core/login.html")


def logout_view(request):
    logout(request)
    return redirect("core:login")


@login_required
def dashboard(request):
    profile = request.user.profile
    return render(request, "core/dashboard.html", {"profile": profile})
