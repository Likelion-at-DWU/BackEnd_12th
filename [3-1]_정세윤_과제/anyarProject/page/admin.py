from django.contrib import admin
from .models import Post # 같은 폴더 내의 models에서 작성한 Post를 import하겠다.

# Register your models here.
admin.site.register(Post) # 관리자 사이트에 Post를 등록하겠다.