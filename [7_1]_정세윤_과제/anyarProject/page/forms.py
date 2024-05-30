from django import forms # django에서 제공하는 forms 기능 import
from .models import Post, Comment

class PostModelForm(forms.ModelForm): # PostModelForm이라는 이름의 모델 폼 클래스 생성
    class Meta:
        model = Post # Meta 클래스 안에 form에서 사용할 모델이 Post임을 명시
        fields = ['title', 'body', 'photo']  # Post 모델에서 입력 받고 싶은 필드를 리스트 형태로 작성

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment 
        fields = ['comment']
