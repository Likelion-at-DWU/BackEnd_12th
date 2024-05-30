from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name="제목", max_length=128)
    body = models.TextField(verbose_name="내용", default="")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    photo = models.ImageField(verbose_name="이미지", blank=True, null=True, upload_to='blog_photo')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    liked_users = models.ManyToManyField(User, related_name='liked_posts')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.CharField(verbose_name="댓글", max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    linked_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.content