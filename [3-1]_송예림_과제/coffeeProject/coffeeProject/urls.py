"""
URL configuration for coffeeProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from coffee import views

urlpatterns = [
    path('admin/', admin.site.urls), #urls.py에 기본적으로 들어가 있는 코드
    path("", views.home, name='home'),
    path("about/", include("about.urls")),
    path("products/", include("products.urls")),
    path("store/", include("store.urls")),
    path('create/', views.create, name='create'),
]
