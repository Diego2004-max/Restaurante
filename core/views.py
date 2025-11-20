# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from .models import Profile


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            
            role = form.cleaned_data["role"]

           
            profile, created = Profile.objects.get_or_create(
                user=user,
                defaults={"role": role},
            )

            if not created:
                profile.role = role
                profile.save()

            login(request, user)
            return redirect("core:dashboard")
    else:
        form = RegisterForm()

    return render(request, "core/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("core:dashboard")
        return render(request, "core/login.html", {"error": "Credenciales incorrectas"})

    return render(request, "core/login.html")


def logout_view(request):
    logout(request)
    return redirect("core:login")


def home(request):
    return render(request, "core/home.html")


@login_required
def dashboard(request):
    
    profile, created = Profile.objects.get_or_create(
        user=request.user,
        defaults={"role": "cliente"},
    )

    role = profile.role
    context = {"profile": profile}

    if role == "admin":
        context["admin_view"] = True
    elif role == "mesero":
        context["mesero_view"] = True
    else:
        context["cliente_view"] = True

    return render(request, "core/dashboard.html", context)
