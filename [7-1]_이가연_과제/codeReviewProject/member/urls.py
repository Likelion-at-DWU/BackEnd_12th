from django.contrib import admin
from django.urls import path
from member import views

urlpatterns = [
    path("", views.member, name="member"),
]