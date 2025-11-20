from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('core.urls')),
    path('menu/', include('menu.urls')),
    path('inventory/', include('inventory.urls')),
    path('orders/', include('orders.urls')),
    path('reservations/', include('reservations.urls')),
    path('reports/', include('reports.urls')),
]
