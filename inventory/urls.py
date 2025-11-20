from django.urls import path
from . import views

app_name = "inventory"

urlpatterns = [
    path("", views.inventory_list, name="list"),
    path("movement/create/", views.movement_create, name="movement_create"),
]
