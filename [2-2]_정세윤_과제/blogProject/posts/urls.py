from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path("", views.post, name="posts"),
]