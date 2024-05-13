from django.contrib import admin
from django.urls import path
from spring import views

urlpatterns =[
    path("", views.spring, name="spring"),
    path('spring/<int:post_id>/', views.post_detail, name='post_detail'),
    path("spring/post_update/<int:id>/", views.post_update, name="post_update"),
    path("post_delete/<int:id>/", views.post_delete, name="post_delete"),
    path('create_comment/<int:id>', views.create_comment, name='create_comment'),
    path('update_comment/<int:post_id>/<int:com_id>', views.update_comment, name='update_comment'),
    path('delete_comment/<int:post_id>/<int:com_id>', views.delete_comment, name='delete_comment'),
]