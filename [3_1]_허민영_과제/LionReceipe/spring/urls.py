from django.contrib import admin
from django.urls import path
from spring import views

urlpatterns =[
    path("", views.spring, name="spring"),
]