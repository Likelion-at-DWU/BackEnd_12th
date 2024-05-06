from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path("", views.product, name="products"),
    path("product_list", views.product_list, name="product_list"),
    path("product_detail/<int:product_id>/", views.product_detail, name="product_detail"),
    path("product_update/<int:id>/", views.product_update, name="product_update"),
    path("product_delete/<int:id>/", views.product_delete, name="product_delete"),
]