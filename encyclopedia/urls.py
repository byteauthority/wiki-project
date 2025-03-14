from django.urls import path

from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("wiki/<str:title>", views.open, name="open")
]
