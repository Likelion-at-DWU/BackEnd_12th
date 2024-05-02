from django.contrib import admin
from django.urls import path
from post import views

urlpatterns = [
    path("", views.post, name="post"),
]