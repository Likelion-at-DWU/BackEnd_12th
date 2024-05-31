from django.db import models
from django.contrib.auth.models import User

class Review(models.Model) : 
    project_name = models.CharField(verbose_name="프로젝트명", max_length=128)
    language = models.CharField(verbose_name="언어", max_length=128)
    code = models.TextField(verbose_name="코드내용", default="")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    photo = models.ImageField(verbose_name="이미지", blank=True, null=True, upload_to='review_photo')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.project_name


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.comment