from django import forms
from .models import Post, Comment

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'photo']  #모델에서 입력받고 싶은 필드를 리스트 형태로
                                    #모든 필드를 다 입력받으려면 fields='__all__'
                                    
class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment 
        fields = ['comment'] #Comment 모델의 comment 필드만 입력 받겠다
                                