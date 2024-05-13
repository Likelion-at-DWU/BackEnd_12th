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

    # 댓글 작성, 조회
    path('create_comment/<int:id>', views.create_comment, name='create_comment'),

    # 댓글 수정(업데이트)
    path('update_comment/<int:book_id>/<int:com_id>', views.update_comment, name='update_comment'),

    # 댓글 삭제
    path('delete_comment/<int:book_id>/<int:com_id>', views.delete_comment, name='delete_comment'),
]
