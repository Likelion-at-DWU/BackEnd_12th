from django.contrib import admin
from django.urls import path
from project import views

urlpatterns = [
    path("", views.project, name="project"),
]