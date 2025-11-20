from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("core.urls")),
    path("menu/", include("menu.urls")),
    path("orders/", include("orders.urls")),
    path("inventory/", include("inventory.urls")),
    path("reservations/", include("reservations.urls")),
    path("reports/", include("reports.urls")),
    path("admin/", admin.site.urls),
]
