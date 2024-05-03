from django.contrib import admin
from django.urls import path
from returning import views

urlpatterns = [
    path("", views.returning, name="returning"), # 첫번째 path
]
