from django.db import models

# Create your models here.
class SpringFood(models.Model):
    title = models.CharField(verbose_name="제목", max_length=128)
    body = models.TextField(verbose_name="내용", default="")
    image = models.ImageField(verbose_name="이미지", blank=True, null=True, upload_to="spring_photo")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    
    def __str__(self): #admin에서 글 제목을 표시.
        return self.title
    
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(SpringFood, on_delete=models.CASCADE)

    def __str__(self): 
        return self.comment