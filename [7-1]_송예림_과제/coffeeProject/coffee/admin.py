from django.contrib import admin
from .models import Post, Comment

# Register your models here. 작성한 모델을 관리하기 위해 등록해야함
admin.site.register(Post) #관리자 사이트에 Post 등록
admin.site.register(Comment)