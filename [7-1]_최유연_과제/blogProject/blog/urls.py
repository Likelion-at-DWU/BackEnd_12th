# blog앱 내부의 urls.py 파일생성
from django.contrib import admin
from django.urls import path,include
from blog import views

urlpatterns = [
    path("", views.home, name="home"), # 첫번째 path
    path("create/", views.home, name="home"), # 두번째 path
    path("home/", include("blog.urls")),
]
