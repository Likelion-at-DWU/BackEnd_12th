from django.contrib import admin
from .models import Post, Comment

# admin 페이지에서 볼 수 있도록 추가
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)