from django import forms
from .models import Post, Comment

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'photo'] 

        widgets = {
            'body': forms.Textarea(
                attrs={'placeholder': '구매 장소와 가격을 꼭 포함해서 리뷰해주세요!'}),
        }

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment 
        fields = ['comment']