from django.db import models

# Create your models here.
class SpringFood(models.Model):
    title = models.CharField(verbose_name="제목", max_length=128)
    body = models.TextField(verbose_name="내용", default="")
    image = models.ImageField(upload_to="%Y/%m/%d")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    
    def __str__(self): #admin에서 글 제목을 표시.
        return self.title