from django.contrib import admin
from django.urls import path
from review import views

urlpatterns = [
    path("", views.review, name="review"),

    # 리뷰 목록을 조회하기 위한 url 생성
    path("review_list", views.review_list, name="review_list"),
    
    # 상세 페이지 구현
    path("review_detail/<int:review_id>/", views.review_detail, name="review_detail"),

    # 수정 페이지 구현
    path("review_update/<int:review_id>/", views.review_update, name="review_update"),

    # 삭제 페이지 구현
    path("review_delete/<int:review_id>/", views.review_delete, name="review_delete"),

    # 댓글 생성 
    path('create_comment/<int:review_id>', views.create_comment, name='create_comment'),

    # 댓글 수정
    path('update_comment/<int:review_id>/<int:com_id>/', views.update_comment, name='update_comment'),

    # 댓글 삭제
    path('delete_comment/<int:review_id>/<int:com_id>', views.delete_comment, name='delete_comment'),
]