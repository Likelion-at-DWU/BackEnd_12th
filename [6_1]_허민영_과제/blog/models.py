from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name = "제목", max_length = 128)
    info = models.TextField(verbose_name = "정보", default = "")
    receipe = models.TextField(verbose_name = "레시피", default = "")
    created_at = models.DateTimeField(verbose_name = "작성일", auto_now_add = True)
    photo = models.ImageField(verbose_name="이미지", blank=True, null=True, upload_to='blog_photo')
    author = models.ForeignKey(User,on_delete=models.CASCADE, null = True)
    rating = models.DecimalField(verbose_name="평균 등급", max_digits=3, decimal_places=2, default = 0 , blank=True)

    def __str__(self):
        return self.title
    
    def update_rating(self):
        comments = self.comment_set.all()
        if comments.exists():
            average_grade = comments.aggregate(models.Avg('grade'))['grade__avg']
            self.rating = round(average_grade, 2)
        else:
            self.rating = None
        self.save()

    
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    date = models.DateField(auto_now_add=True)
    article=models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.comment