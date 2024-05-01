from django.contrib import admin
from django.urls import path
from reviews import views

urlpatterns = [
    path("", views.post, name="reviews"),
]