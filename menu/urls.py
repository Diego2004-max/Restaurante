from django.urls import path
from . import views

app_name = "menu"

urlpatterns = [
    path("", views.menu_list, name="list"),
    path("crear/", views.menu_create, name="create"),
    path("<int:pk>/editar/", views.menu_edit, name="edit"),
    path("<int:pk>/eliminar/", views.menu_delete, name="delete"),
]
