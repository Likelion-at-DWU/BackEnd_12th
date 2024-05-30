from django.contrib import admin
from django.urls import path
from single import views

urlpatterns = [
    path("", views.single, name="single"),
]
