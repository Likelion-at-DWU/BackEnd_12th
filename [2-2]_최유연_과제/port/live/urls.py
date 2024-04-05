from django.contrib import admin
from django.urls import path
from live import views

urlpatterns = [
    path("",views.home,name="home"),
    path("create/",views.home,name="home"),
]