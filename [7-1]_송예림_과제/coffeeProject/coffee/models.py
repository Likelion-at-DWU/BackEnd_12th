from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Post(models.Model):  #Post 클래스-3개의 필드 가짐

    title = models.CharField(verbose_name="제목", max_length=128)
    body = models.TextField(verbose_name="내용", default="")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    photo = models.ImageField(verbose_name="이미지", blank=True, null=True, upload_to='blog_photo')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    like_users = models.ManyToManyField(User, related_name='like_posts')
    def __str__(self):  #admin에서 글 제목 표시 
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Post, on_delete=models.CASCADE) #on_delete=models.CASCADE: 참조하고 있는 Post 사라지면 Comment도 사라짐
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self): 
        return self.comment