from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path("", views.blog, name="blog"),
    path("post_list", views.post_list, name="post_list"),
    path("post_detail/<int:post_id>/", views.post_detail, name="post_detail"),
    path("post_update/<int:id>/", views.post_update, name="post_update"),
    path("post_delete/<int:id>/", views.post_delete, name="post_delete"),
    path('create_comment/<int:id>', views.create_comment, name='create_comment'),
    path('update_comment/<int:post_id>/<int:com_id>', views.update_comment, name='update_comment'),
    path('delete_comment/<int:post_id>/<int:com_id>', views.delete_comment, name='delete_comment'),
    path('<int:post_id>/bookmark/', views.bookmark, name='bookmark'),
    path('bookmark_list', views.bookmark_list, name='bookmark_list'),
]
