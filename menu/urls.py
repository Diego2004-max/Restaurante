from django.urls import path
from . import views

app_name = "menu"

urlpatterns = [
    path("dishes/", views.dish_list, name="dish_list"),
    path("dishes/create/", views.dish_create, name="dish_create"),
    path("ingredients/", views.ingredient_list, name="ingredient_list"),
    path("ingredients/create/", views.ingredient_create, name="ingredient_create"),
]
