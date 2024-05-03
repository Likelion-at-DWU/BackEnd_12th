from django.contrib import admin
from django.urls import path
from borrow import views

urlpatterns = [
    path("", views.borrow, name="borrow"), # 첫번째 path
]
