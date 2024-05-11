from django.contrib import admin
from .models import Post, Comment

# Register your models here.
admin.site.register(Post) # 관리자 사이트에 Post를 등록하겠다.
admin.site.register(Comment)