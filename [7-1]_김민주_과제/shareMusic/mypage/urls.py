from django.contrib import admin
from django.urls import path
from mypage import views

urlpatterns = [
    path('', views.mypage, name='mypage'),
    path('myposts/', views.myposts, name='myposts'),
    path('mycomments/', views.mycomments, name='mycomments'),
    path('mylikes/', views.mylikes, name='mylikes'),
    path('mylikes/unlike/<int:post_id>/', views.unlike_post, name='unlike_post'),
]