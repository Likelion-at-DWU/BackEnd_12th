"""
URL configuration for LionReceipe project.

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
from blog import views as blog_views  # 블로그 앱에서 view 모듈을 가져옴
from spring import views as spring_views  # Spring 앱에서 view 모듈을 가져옴
from summer import views as summer_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", blog_views.home, name="home"), #블로그앱에 작성한 view함수 연결
    path("posts/", include("post.urls")),
    path('create/', blog_views.create, name='create'),
    path('spring/',include("spring.urls")),
    path('spring/createSpringFood/', spring_views.createSpringFood, name="createSpringFood"),
    path('summer/',include("summer.urls")),
    path('summer/createSummerFood/', summer_views.createSummerFood, name="createSummerFood"),
    path('spring/<int:post_id>/', spring_views.post_detail, name='post_detail'),  #봄 카테고리 (최신글)글 상세조회
] 

urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)