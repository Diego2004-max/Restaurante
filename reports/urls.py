from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [
    path("top-dishes/", views.top_dishes_pdf, name="top_dishes"),
]
