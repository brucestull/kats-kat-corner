from django.urls import path

from kat_corner import views

app_name = "kat_corner"
urlpatterns = [
    path("", views.index, name="index"),
]
