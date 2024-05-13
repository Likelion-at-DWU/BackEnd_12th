from django.urls import path
from accounts import views

#namespace 가 accounts 라는 이름을 가졌음을 명시
app_name = "accounts" 

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
