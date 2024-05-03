from django.db import models

# Create your models here.
class Book(models.Model) : 
    title = models.CharField(verbose_name="제목", max_length=128)
    author = models.CharField(verbose_name="저자",max_length=10)
    contents = models.TextField(verbose_name="내용", default="")
    publish_date = models.DateTimeField(verbose_name="출판일", auto_now_add=True)

    def __str__(self):  #admin에서 글 제목을 표시한다. 
        return self.title