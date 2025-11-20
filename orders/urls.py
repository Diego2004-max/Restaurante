from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("menu/", views.menu_view, name="menu"),
    path("cart/", views.cart, name="cart"),
    path("add/<int:dish_id>/", views.add_to_cart, name="add"),
    path("pay/", views.pay_order, name="pay"),
    path("history/", views.history, name="history"),
]
