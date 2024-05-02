from django.db import models

# Create your models here.
class Post(models.Model):  #Post 클래스-3개의 필드 가짐

    title = models.CharField(verbose_name="제목", max_length=128)
    body = models.TextField(verbose_name="내용", default="")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)

    def __str__(self):  #admin에서 글 제목 표시 
        return self.title