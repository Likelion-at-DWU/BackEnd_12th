from django.contrib import admin
from django.urls import path
from page import views

urlpatterns = [
    path("", views.page, name="page"),
    path("create/", views.page, name='page'),
]
