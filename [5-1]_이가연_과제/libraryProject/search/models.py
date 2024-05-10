from django.db import models # type: ignore


# Create your models here.
class Book(models.Model) : 
    title = models.CharField(verbose_name="제목", max_length=128)
    author = models.CharField(verbose_name="저자",max_length=10)
    contents = models.TextField(verbose_name="내용", default="")
    created_at = models.DateTimeField(verbose_name="출판일", auto_now_add=True)
    photo = models.ImageField(verbose_name="이미지", blank=True, null=True, upload_to='book_photo')

    def __str__(self):  #admin에서 글 제목을 표시한다. 
        return self.title
    
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.comment