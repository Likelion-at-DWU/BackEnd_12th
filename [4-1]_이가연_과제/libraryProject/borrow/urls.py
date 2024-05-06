from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from borrow import views

urlpatterns = [
    # 첫번째 path
    path("", views.borrow, name="borrow"),

    # 책 목록을 조회하기 위한 url 생성
    path("book_list", views.book_list, name="book_list"),

    # 상세 페이지 구현
    path("book_detail/<int:book_id>/", views.book_detail, name="book_detail"),

    # 업데이트
    path("book_update/<int:book_id>/", views.book_update, name="book_update"),

    # 삭제
    path("book_delete/<int:id>/", views.book_delete, name="book_delete"),
]
