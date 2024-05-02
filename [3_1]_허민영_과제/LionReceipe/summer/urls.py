from django.contrib import admin
from django.urls import path
from summer import views

urlpatterns = [
    path("", views.summer, name="summer")
]
