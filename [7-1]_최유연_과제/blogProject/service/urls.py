from django.contrib import admin
from django.urls import path
from service import views

urlpatterns = [
    path("", views.service, name="service"),
]
