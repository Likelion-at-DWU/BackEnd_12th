from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path("", views.product, name="products"),
    path("product_list", views.product_list, name="product_list"),
    path("product_detail/<int:product_id>/", views.product_detail, name="product_detail"),
    path("product_update/<int:id>/", views.product_update, name="product_update"),
    path("product_delete/<int:id>/", views.product_delete, name="product_delete"),
    path('create_comment/<int:id>', views.create_comment, name='create_comment'),
    path('update_comment/<int:product_id>/<int:com_id>', views.update_comment, name='update_comment'),
    path('delete_comment/<int:product_id>/<int:com_id>', views.delete_comment, name='delete_comment'),
    path("product_detail/<int:product_id>/like/", views.like_post, name="like_post"),
]