from django.contrib import admin
from django.urls import path 
from store import views

urlpatterns = [
    path("", views.store, name="store"),
    path("post_list", views.post_list, name="post_list"),
    path("post_detail/<int:post_id>/", views.post_detail, name="post_detail"),
    path("post_update/<int:id>/", views.post_update, name="post_update"),
    path("post_delete/<int:id>/", views.post_delete, name="post_delete")
]
